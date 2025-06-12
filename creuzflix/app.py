import streamlit as st
import pandas as pd
import requests

# Configuration initiale
st.set_page_config(page_title="Creuzflix", layout="wide", initial_sidebar_state="collapsed")

# --- Chargement des données ---
data = "https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Nathan/creuzflix/Movies.csv"
df = pd.read_csv(data, sep='\t', low_memory=False)

# --- Préparation des films par popularité ---
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
df_sorted = df.sort_values(by="popularity", ascending=False)

top5_populaires = df_sorted.head(5)
next15_populaires = df_sorted.iloc[5:20]

# --- CSS personnalisé ---
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
.film-card:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
}
.block-container {
    padding-top: 2rem !important;
}
.featured-row {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    overflow: hidden;
}
.featured-item {
    flex: 1;
    transition: flex 0.3s ease-in-out, transform 0.3s ease-in-out;
}
.featured-item:hover {
    flex: 2;
    transform: scale(1.03);
    z-index: 1;
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
col1, col2, col3 = st.columns([1.2, 6, 1])
with col1:
    st.image("https://i.imgur.com/aTk9bwU.png", width=288)

with col2:
    cols = st.columns([0.2, 0.2, 0.2, 0.2, 0.2])
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

# --- Zone de recherche ---
if st.session_state.get("show_search", False):
    search = st.text_input("Rechercher un film", "")

# --- Section "Films mis en avant" ---
st.markdown('<h2 class="section-title">🎞️ Films mis en avant</h2>', unsafe_allow_html=True)
# Affichage horizontal via des colonnes Streamlit
cols = st.columns(len(top5_populaires))

for col, (_, row) in zip(cols, top5_populaires.iterrows()):
    with col:
        img_url = f"https://image.tmdb.org/t/p/w500{row['poster_path']}" if pd.notna(row['poster_path']) else "https://via.placeholder.com/300x450?text=No+Image"
        st.image(img_url, use_container_width=True)
        st.caption(row["title_x"])


import streamlit.components.v1 as components

# --- Section "Films populaires" dynamique ---
st.markdown('<h2 class="section-title">🔥 Films populaires</h2>', unsafe_allow_html=True)

# Récupération de 16 films (5 premiers déjà utilisés)
next16_populaires = df_sorted.iloc[5:21]

# Construction HTML en grid responsive
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

# Affichage dans Streamlit
components.html(pop_html, height=950, scrolling=False)
