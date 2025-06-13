import streamlit as st
import pandas as pd
import numpy as np
from streamlit_searchbox import st_searchbox
from modules import ml
import streamlit.components.v1 as components

# --- Config ---
st.set_page_config(page_title="Creuzflix", layout="wide", initial_sidebar_state="collapsed")

# --- Données ---
df = pd.read_csv("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Nathan/creuzflix/Movies.csv", sep='\t', low_memory=False)
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
df_sorted = df.sort_values(by="popularity", ascending=False)
top5_populaires = df_sorted.head(5)
next16_populaires = df_sorted.iloc[5:21]
base = pd.read_csv("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Base_films_v2.csv", sep='\t')
liste_films = base['Title'].unique().tolist()

# --- CSS global ---
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
    font-weight: normal;
    font-size: 0.8rem;
    padding: 0.3rem 0.6rem;
    border: none;
    border-radius: 10px;
    transition: all 0.2s ease;
    cursor: pointer;
    margin-top: 0.3rem;
    width: 100%;
    text-align: center;
}
.stButton > button:hover {
    background-color: #333333 !important;
    transform: scale(1.02);
}
.featured-item img {
    width: 100%;
    border-radius: 8px;
    max-height: 320px;
    object-fit: cover;
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
    background-size: cover;
    opacity: 1;
    z-index: 0;
    pointer-events: none;
}
</style>
<div class="background-overlay"></div>
""", unsafe_allow_html=True)

# --- Navigation ---
col1, col2, _ = st.columns([1.2, 6, 1])
with col1:
    st.image("https://i.imgur.com/aTk9bwU.png", width=288)
with col2:
    cols = st.columns([0.2, 0.2, 0.2, 0.2])
    for col in cols:
        with col:
            st.markdown("<div style='margin-top:100px'></div>", unsafe_allow_html=True)

    with cols[0]:
        if st.button("🔍 Recherche"):
            st.session_state.show_search = not st.session_state.get("show_search", False)
    with cols[1]:
        if st.button("🎬 Films"):
            st.switch_page("pages/films.py")
    with cols[2]:
        if st.button("📂 Genres"):
            st.switch_page("pages/genres.py")
    with cols[3]:
        if st.button("🎭 Acteurs"):
            st.switch_page("pages/acteurs.py")

# --- Tuiles cliquables ---
def display_recommendation_tile(rec_title, rec_url, i):
    st.image(rec_url, use_container_width=True)
    if st.button(f"🎥 {rec_title}", key=f"rec_btn_{i}"):
        st.session_state.selected_film = rec_title
        st.session_state.film_changed = True
        if 'film_search_reveal' in st.session_state:
            del st.session_state['film_search_reveal']
        st.rerun()

# --- Affichage fiche film ---
def display_film_info(film_title):
    recommandations = ml.recommend_movies_dbscan(film_title, n_recommendations=5)
    film_info = base[base["Title"] == film_title].iloc[0]
    poster_path = df[df["title_x"] == film_title]["poster_path"].values
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path[0]}" if len(poster_path) > 0 and pd.notna(poster_path[0]) else "https://via.placeholder.com/300x450?text=No+Image"

    st.markdown('<h2 class="section-title">🎬 Film sélectionné</h2>', unsafe_allow_html=True)
    col_g, col_d = st.columns([1, 4])
    with col_g:
        st.image(poster_url, width=300)
    with col_d:
        st.markdown(f"### {film_info['Title']}")
        st.markdown(f"⭐⭐⭐ Note : {film_info['note']} / 10")
        st.markdown(f"Acteurs : {film_info.get('leading_role', '--')}, {film_info.get('second_role', '--')}, {film_info.get('third_role', '--')}")
        st.markdown("**Synopsis :**")
        st.markdown(film_info['synopsis'] if pd.notna(film_info['synopsis']) else "_Pas de synopsis disponible._")

    if not recommandations.empty:
        st.markdown('<h2 class="section-title">🎯 Recommandations similaires</h2>', unsafe_allow_html=True)
        recommandations_limited = recommandations.head(8)
        cols_rec = st.columns(len(recommandations_limited))
        for i, (col_rec, (_, rec)) in enumerate(zip(cols_rec, recommandations_limited.iterrows())):
            with col_rec:
                rec_title = rec["Title"]
                rec_path = df[df["title_x"] == rec_title]["poster_path"].values
                rec_url = f"https://image.tmdb.org/t/p/w500{rec_path[0]}" if len(rec_path) > 0 and pd.notna(rec_path[0]) else "https://via.placeholder.com/300x450?text=No+Image"
                display_recommendation_tile(rec_title, rec_url, i)

# --- Recherche ---
if st.session_state.get("show_search", False):
    selected_film = st_searchbox(lambda term: [f for f in liste_films if term.lower() in f.lower()][:7], placeholder="Rechercher un film...", key="film_search_reveal")
    current_film = None
    if st.session_state.get('film_changed', False):
        current_film = st.session_state.selected_film
        st.session_state.film_changed = False
    elif selected_film:
        current_film = selected_film
        st.session_state.selected_film = selected_film
    elif 'selected_film' in st.session_state:
        current_film = st.session_state.selected_film
    if current_film:
        display_film_info(current_film)

# --- Films mis en avant ---
st.markdown('<h2 class="section-title">🎞️ Films mis en avant</h2>', unsafe_allow_html=True)
cols = st.columns(len(top5_populaires))
for col, (_, row) in zip(cols, top5_populaires.iterrows()):
    with col:
        img_url = f"https://image.tmdb.org/t/p/w500{row['poster_path']}" if pd.notna(row['poster_path']) else "https://via.placeholder.com/300x450?text=No+Image"
        st.image(img_url, use_container_width=True)
        st.caption(row["title_x"])

# --- Films populaires ---
st.markdown('<h2 class="section-title">🔥 Films populaires</h2>', unsafe_allow_html=True)
pop_html = """
<style>
.pop-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 20px;
    padding: 10px 0;
}
.pop-card {
    text-align: center;
    transition: transform 0.3s ease-in-out;
}
.pop-card:hover {
    transform: scale(1.05);
}
.pop-card img {
    width: 100%;
    height: 270px;
    object-fit: cover;
    border-radius: 10px;
}
.pop-card p {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: white;
}
</style>
<div class="pop-grid">
"""
for _, row in next16_populaires.iterrows():
    img_url = f"https://image.tmdb.org/t/p/w500{row['poster_path']}" if pd.notna(row['poster_path']) else "https://via.placeholder.com/300x450?text=No+Image"
    title = row["title_x"]
    pop_html += f"""
    <div class="pop-card">
        <img src="{img_url}" alt="{title}">
        <p>{title}</p>
    </div>
    """
pop_html += "</div>"
components.html(pop_html, height=950, scrolling=False)

