import streamlit as st
import requests

# Configuration initiale de la page
st.set_page_config(page_title="Acteurs - Creuzflix", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS pour hover effets
st.markdown("""
<style>
html, body, .main, .block-container, .stApp {
    background-color: #0f0f0f !important;
    color: white !important;
}

h2.section-title {
    font-size: 1.4rem;
    font-weight: bold;
    color: white;
    margin-bottom: 1rem;
    margin-top: 2rem;
}

.stButton > button {
    background-color: transparent;
    color: white !important;
    font-weight: bold;
    font-size: 2.2rem;
    padding: 1.2rem 2.4rem;
    border: none;
    border-radius: 999px;
    transition: background-color 0.3s ease;
    cursor: pointer;
    margin-left: 0.3rem;
    margin-right: 0.3rem;
    margin-top: 6rem;
}

.stButton > button:hover {
    background-color: #333333 !important;
}

.actor-card {
    text-align: center;
    margin-bottom: 1rem;
}

.actor-card img {
    width: 80px;
    height: auto;
    border-radius: 12px;
    margin-bottom: 0.5rem;
}
.background-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(to bottom, rgba(15, 15, 15, 1) 30%, rgba(15, 15, 15, 0.2) 95%),
        linear-gradient(to right, rgba(15, 15, 15, 0.95) 20%, rgba(15, 15, 15, 0.2) 95%),
        url("https://i.imgur.com/jMVyaCh.png");
    background-repeat: no-repeat, no-repeat, no-repeat;
    background-position: center bottom, right center, center center;
    background-size: cover, cover, cover;
    opacity: 1;
    z-index: 0;
    pointer-events: none;
}
</style>
<div class="background-overlay"></div>
""", unsafe_allow_html=True)

# --- Bandeau supérieur ---
col1, col2, col3 = st.columns([1.2,6,1])
with col1:
    st.image("https://i.imgur.com/aTk9bwU.png", width=288)

with col2:
    cols = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
    with cols[0]:
        if st.button("🏠 Accueil"):
            st.switch_page("app.py")
    with cols[1]:
        if st.button("🎬 Films"):
            st.switch_page("pages/films.py")
    with cols[2]:
        if st.button("📂 Genres"):
            st.switch_page("pages/genres.py")
    with cols[3]:
        if st.button("🎭 Acteurs"):
            st.switch_page("pages/acteurs.py")

# Champ de recherche
st.markdown('<h2 class="section-title">🔍 Rechercher un acteur</h2>', unsafe_allow_html=True)
search = st.text_input("Entrez un nom d'acteur")

# Acteurs populaires
st.markdown('<h2 class="section-title">🌟 Acteurs populaires</h2>', unsafe_allow_html=True)

API_KEY = "2b072728b0ab020d89028cedf8b86cd1"
url = f"https://api.themoviedb.org/3/person/popular?api_key={API_KEY}&language=fr-FR&page=1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    popular_actors = data["results"][:40]
    rows = [popular_actors[i:i+10] for i in range(0, len(popular_actors), 10)]
    for row in rows:
        cols = st.columns(10)
        for actor, col in zip(row, cols):
            with col:
                st.markdown(f"""
                    <div class='actor-card'>
                        <img src=\"https://image.tmdb.org/t/p/w185{actor['profile_path']}\" alt=\"{actor['name']}\">
                        <div>{actor['name']}</div>
                    </div>
                """, unsafe_allow_html=True)
else:
    st.error("Impossible de récupérer les acteurs populaires.")
