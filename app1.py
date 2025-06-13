import streamlit as st
import pandas as pd

# Titre principal
st.title("Projet : Recommandation de films")

# Section Objectif et Problématique (en colonnes)
col1, col2 = st.columns(2)

with col1:
    st.header("Objectif")
    st.markdown("""
    🎬 **L'objectif est de mettre en place un système de recommandation de films...**
    """)

with col2:
    st.header("Problématique")
    st.markdown("""
    ⚠️ **Votre cinéma est actuellement en perte de vitesse avec une baisse du chiffre d'affaires.**
    """)

# Section Besoin client et Contraintes (en colonnes)
col3, col4 = st.columns(2)

with col3:
    st.header("Besoin client")
    st.markdown("""
    💛 **Disposer d'un outil pour la recommandation de films...**
    """)

with col4:
    st.header("Contraintes")
    st.markdown("""
    🔧 **Aucune donnée interne sur les goûts des clients...**
    """)

# Section Votre métier
st.header("Votre métier")
st.markdown("""
🌐 **Cinéma situé dans la Creuse.**
""")

# Section Rétroplanning
st.header("Rétroplanning")
st.subheader("Voici le rétroplanning du projet.")
data = {
    "Étape": [
        "0. Réaliser une étude de marché sur la consommation de cinéma dans la Creuse",
        "1. Réaliser une étude de marché sur la consommation de cinéma dans la Creuse",
        "2. Appropriation, exploration des données et nettoyage (Pandas, Matplotlib, Seaborn)",
        "3. Début création maquette sous Streamlit",
        "4. Machine learning et recommandations (scikit-learn)",
        "5. Amélioration maquette Streamlit, test algo de recommandation et création des statistiques",
        "6. Affinement et amélioration fluidité / rapidité du site, modification des fonctions, affichage de l'interface et préparation de la présentation"
    ],
    "Timing": [
        "Semaine 1",
        "Semaine 2",
        "Semaine 3",
        "Semaine 4",
        "Semaine 5",
        "Semaine 6",
        "Semaine 7"
    ],
    "Statut": ["✅", "✅", "✅", "✅", "✅", "✅", "✅"]
}

df = pd.DataFrame(data)
st.table(df)

# Section Outils et technologies
st.header("Les outils et techno pour ce projet")

# Langages
st.subheader("Langages :")
st.markdown("- Python : pour le développement global du projet.")
st.markdown("- HTML et CSS : pour la mise en page, le design et les effets sur les pages, textes et images.")

# Gestion et nettoyage des données
st.subheader("Gestion et nettoyage des données :")
st.markdown("- Expressions régulières (re) : pour le nettoyage et la manipulation textuelle.")

# APIs utilisées
st.subheader("APIs utilisées :")
st.markdown("- API TMDB (The Movie Database) : pour la création de la base de données, les images des films, des acteurs etc. (titres, genres, notes, acteurs, etc.).")
st.markdown("- API OpenAI : pour la génération de mots-clés à partir des synopsis.")

# Développement de l'interface utilisateur
st.subheader("Développement de l'interface utilisateur :")
st.markdown("- Streamlit : création rapide et interactive d'applications web pour afficher les résultats et interagir avec les utilisateurs.")

# Collaborations et versioning
st.subheader("Collaborations et versioning :")
st.markdown("- GitHub et GitHub Desktop : pour le contrôle de version et la collaboration.")

# Bibliothèques de manipulation des données
st.subheader("Librairies de manipulation des données :")
st.markdown("- Pandas : analyse et transformation des données.")
st.markdown("- NumPy : opérations mathématiques et manipulation efficace des tableaux.")

# Bibliothèques pour la recommandation et le machine learning
st.subheader("Librairies pour la recommandation et le machine learning :")
st.markdown("- Scikit-learn : calcul de similarité, algorithmes de recommandation et outils d'apprentissage automatique.")

# Bibliothèques pour la visualisation des données
st.subheader("Bibliothèques pour la visualisation des données :")
st.markdown("- Matplotlib, Plotly-Express et Seaborn : visualisation de données pour comprendre les tendances et les distributions.")