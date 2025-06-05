import streamlit as st

st.set_page_config(page_title="Films - Creuzflix", layout="wide", initial_sidebar_state="collapsed")

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


st.title("🎬 Tous les films")

st.markdown("Voici une sélection de films disponibles (placeholders pour l'instant).")

for _ in range(3):
    cols = st.columns(4)
    for col in cols:
        with col:
            st.image("https://via.placeholder.com/200x300", use_container_width=True)
            st.caption("Titre du film")

