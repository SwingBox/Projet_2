# ------------------------------------------------------------------------------------------------------------------------------------------
# Définition de la fonction de recherche et de filtrage dynamique des films
# ------------------------------------------------------------------------------------------------------------------------------------------
# récupération Base_films
base = pd.read_csv("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Base_films_v2.csv", sep = '\t')
liste_films = base['Title'].unique().tolist()

def search_films(term: str) -> list:
    if not term:
        return []
    # Exemple avec une liste locale (à remplacer par ton DataFrame ou une API)
    films = liste_films
    term_lower = term.lower()
    return [titre for titre in films if term_lower in titre.lower()][:7]

# Zone de recherche conditionnelle et moteur ML
if st.session_state.get("show_search", False):
    
    col1, col2, col3 = st.columns([2, 1, 7])
    with col1:
        selected_film = st_searchbox(
            search_films,
            placeholder="Rechercher un film...",
            key="film_search_reveal"
        )

    if selected_film:
        # 📡 Recommandations ML
        recommandations = ml.recommend_movies_dbscan(selected_film, n_recommendations=5)
        # 🔎 Récupération des infos du film sélectionné
        film_info = base[base["Title"] == selected_film].iloc[0]
        # Récupération de l'affiche depuis df (via poster_path)
        poster_path = df[df["title_x"] == selected_film]["poster_path"].values
        
        if len(poster_path) > 0 and pd.notna(poster_path[0]):
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path[0]}"
        
        else:
            poster_url = "https://via.placeholder.com/300x450?text=No+Image"
            # 🧾 Affichage bandeau : affiche + titre + synopsis
            st.markdown('<h2 class="section-title">🎬 Film sélectionné</h2>', unsafe_allow_html=True)
            
            col_g, col_d = st.columns([1, 4])
            with col_g:
                st.image(poster_url, width=300)
            with col_d:
                st.markdown(f"### {film_info['Title']}")
                st.markdown("**Synopsis :**")
                st.markdown(film_info['synopsis'] if pd.notna(film_info['synopsis']) else "_Pas de synopsis disponible._")

        if not recommandations.empty:
            st.markdown('<h2 class="section-title">🎯 Recommandations similaires</h2>', unsafe_allow_html=True)

            # Construction HTML responsive
            import streamlit.components.v1 as components

            rec_html = """
            <style>
            .rec-grid {
                display: flex;
                justify-content: start;
                gap: 20px;
                flex-wrap: nowrap;
                    overflow-x: auto;
                    padding: 10px 0;
                        }
            .rec-card {
                flex: 0 0 auto;
                width: 180px;
                text-align: center;
                transition: transform 0.3s ease-in-out;
                    }
            .rec-card:hover {
                transform: scale(1.05);
                    }
            .rec-card img {
                width: 100%;
                height: 270px;
                object-fit: cover;
                border-radius: 10px;
                    }
            .rec-card p {
                margin-top: 0.5rem;
                font-size: 0.9rem;
                color: white;
                    }
            </style>
            <div class="rec-grid">
            """

            for _, rec in recommandations.iterrows():
                rec_title = rec["Title"]
                rec_path = df[df["title_x"] == rec_title]["poster_path"].values
                rec_url = f"https://image.tmdb.org/t/p/w500{rec_path[0]}" if len(rec_path) > 0 and pd.notna(rec_path[0]) else "https://via.placeholder.com/300x450?text=No+Image"

                rec_html += f"""
                <div class="rec-card">
                    <img src="{rec_url}" alt="{rec_title}">
                    <p>{rec_title}</p>
                </div>
                """

                rec_html += "</div>"
                components.html(rec_html, height=600, scrolling=False)
