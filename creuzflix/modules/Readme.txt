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

# selected_film = st_searchbox(search_films, placeholder="Rechercher un film...", key="film_search")
#

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
          recommandations = ml.recommend_movies_dbscan(selected_film, n_recommendations=10)
          if not recommandations.empty:
            for film in recommandations['Title'].tolist():
                st.write(f"🎬 {film}")

# ------------------------------------------------------------------------------------------------------------------------------------------
# Fin de fonction
# ------------------------------------------------------------------------------------------------------------------------------------------
