import streamlit as st

st.set_page_config(page_title="Préparation des données", layout="wide")
st.markdown("<h1 style='text-align: center;'>EXPLOITATION ET NETTOYAGE DES CSV ImDB et TmDB</h1>", unsafe_allow_html=True)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# Section 1
# ----------------------------------------------------------------------------------------------------------------------------------------------

st.header("1 – Récupération des fichiers .csv sur ImDB et TmDB")

st.markdown("""
            <p style="text-align: justify; font-size: 16px;">
            La première démarche fut de récupérer les fichiers zippés sur les sites ImDB et TmDB. 
            Nous nous sommes rapidement rendu compte du poids des fichiers et de la quantité importantes de lignes pour certains d’entre eux (jusqu’à 92 
            millions de lignes).
                <p>
                Nous avons constaté que ces fichiers comportaient des colonnes d’Id uniques, soit en rapport avec les titres de films (tconst) 
                ou en rapport avec les noms du personnel des équipes (nconst).
                <p>L’idée est alors venue de réaliser une table de relation entre les fichiers :
            </p>
            """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1], gap="large")
with col2:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/streamlitenv/Projet_2_Swimbox/Prepa_donnees/Table des relations.png", use_container_width=True)

st.markdown("<p><p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1], gap="large")
with col2:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/streamlitenv/Projet_2_Swimbox/Prepa_donnees/Détail relations.png", use_container_width=True)

# ***************************

st.header("2 – Nettoyage et jointure des fichiers")

st.markdown("""
            <p style="text-align: justify; font-size: 16px;">
            D’une manière plus générale et pour ne pas avoir à détailler tous nos choix, après avoir réalisé quelques statistiques sur les colonnes 
            et les lignes), nous avons supprimé les colonnes qui n’avaient aucun intérêt pour nos features (nature des données, nombre de NaN ou de antislash N 
            en trop grande importance).
                <p>
                D’une manière plus générale et pour ne pas avoir à détailler tous nos choix, après avoir réalisé quelques statistiques sur les colonnes et 
                les lignes), nous avons supprimé les colonnes qui n’avaient aucun intérêt pour nos features (nature des données, nombre de NaN ou de antislash N
                en trop grande importance).
                <p>Une fois cette base prête, nous avons joint les autres fichiers par un ‘left join’ sur title.basics, soit grâce à l’Id tconst, soit grâce
                à l’Id nconst.
                <p>Certains fichiers contenaient des objets de type ‘list’, comme la colonne ‘genres’ de title.basics par exemple. Nous avons extrait les 3 
                principaux éléments pour en faire de nouvelles colonnes.
                <p>Une fois avoir obtenu un seul fichier à partir des csv de ImDB, nous avons fait la jointure avec le fichier TmDB et procédé à un nouveau nettoyage.
                <p>Enfin, pour réduire le nombre de lignes, nous n’avons sélectionné que les films dont la zone était ‘FR’, puis filtré sur le niveau de averageRating
                ainsi que sur le nombre de votes.
                <p>Nous avons par contre gardé certaines colonnes de liste qui provenaient du fichier TmDB, pour les exploiter avec un modèle de transformation ML spécifique.
                <p>L'ensemble des features exploitables étaient contenu dans un DataFrame de 21 colonnes et 10830 lignes. Extrait du df :
            </p>
            """, unsafe_allow_html=True)

st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/streamlitenv/Projet_2_Swimbox/Prepa_donnees/Features.png")

