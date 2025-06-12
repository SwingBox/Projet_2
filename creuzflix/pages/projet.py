import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np

# Import des bibliothèques de viz
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Projet - Creuzflix", layout="wide", initial_sidebar_state="collapsed")

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


st.title("📁 Le Projet")

onglets = st.tabs(["🎯 Le projet", "📊 Analyse", "📈 Statistiques", "🤖Préparation des données et Machine Learning", "👥 L'équipe", "✅ Conclusion"])

with onglets[0]:
    st.header("🎯 Objectif du projet")
    st.markdown("""


Un cinéma indépendant de la Creuse, en perte de vitesse, a décidé de se digitaliser. Il souhaite créer un site capable de recommander des films aux visiteurs, même sans connaître leurs goûts au départ (situation de cold start).

En tant que Data Analysts freelances, notre mission consistait à :
                
   - Étudier le contexte local, pour adapter l’offre aux préférences régionales (cinéma en Creuse).

   - Analyser une base de données de films (issues d’IMDb et TMDB), puis la retravailler: nettoyage, filtrage etc, dans l'optique d'entrainer un modèle de ML de recommandation de films.

   - Construire un système de recommandation de films à partir d’algorithmes de machine learning.

   - Développer une interface en ligne sur Streamlit permettant aux Creusois d'obtenir des recommandations de films.

L’objectif final : offrir aux habitants un service digital en complément du cinéma physique, accessible depuis chez eux.
    """)

with onglets[1]:
    #st.header("📊 Étude de marché & Analyse")
    
    st.markdown("<h1 style='text-align: center;'>📊 ETUDE DEMOGRAPHIQUE ET SECTORIELLE</h1>", unsafe_allow_html=True)
    st.markdown("""<h2 style='text-align: center;'>
        <p>BASEE SUR L‘ACTIVITE DU CINEMA DANS LA CREUSE</p>
        <p>WILD CODE SCHOOL – PROJET 2</p>
    </h2>""", unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------------------------------------------------------------------
    # Section 1
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    st.header("1 – Le département de la Creuse")

    st.subheader("Histoire et localisation de la Creuse")

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.image("https://i.imgur.com/1zgDsiu.png", use_container_width=True)

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 400px;">
                <p style="text-align: justify; font-size: 16px;">Originaire de la province de la Marche, c’est le 4 mars 1790 que fût créé par la Révolution Française le département de la Creuse (23).
                Il est un département Français dont le nom vient du fleuve de la Creuse, affluent de la Vienne et est encore aujourd’hui le 2ème plus petit département Français par sa population avec
                <strong>114 103 habitants estimés en 2025</strong> (0.17% de la population Française).</p>
                <p style="text-align: center; font-weight: bold;">Sources : Wikipédia – Insee.</p>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("La population")

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.image("https://i.imgur.com/Dk67m9b.png")

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 500px;">
                <p style="text-align: justify; font-size: 16px;">
                À l’inverse de la population française, la population de la Creuse est en déclin depuis le 19è siècle (287 000 habitants) 
                en raison du solde naturel négatif (balance natalité – mortalité), bien que légèrement amortie par le solde migratoire (+350 hab/an).  
                En 2021, la population active reste majoritaire, bien que les <strong>60-74 ans</strong> prédominent en nombre. 
                Le <strong>genre féminin</strong> est aussi légèrement plus représenté, surtout après 65 ans.  
                <p><strong>Source : Insee</strong></p>
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    En 2021, la population active reste majoritaire, bien que les **60-74 ans** prédominent en nombre.  
    Le **genre féminin** est aussi légèrement plus représenté, surtout après 65 ans.  
    **Source : Insee**
    """)

    st.image("https://i.imgur.com/c7Ws3mE.png")

    st.subheader("L’économie")

    st.markdown("""
    L’agriculture est la principale source économique dans la Creuse. En 2013 :  
    - Agriculture : **11,9%** de l’emploi total (seul le Gers fait mieux avec 12.2%)  
    - Industrie : **10,7%**  
    - Construction : **6,5%**
    """)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.image("https://i.imgur.com/4WTWoFK.png")

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 300px;">
                <p style="text-align: justify; font-size: 16px;">
                    Les retraités sont logiquement les plus représentés dans les catégories socio-professionnelles, suivis des employés.  
                    Le chômage est élevé mais stable.  
                    Comme au niveau national, les <strong>hommes gagnent plus</strong> en médiane que les femmes.  
                    <p><strong>Source : Insee</strong></p>
                </p>
            </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 300px;">
                <p style="text-align: justify; font-size: 16px;">
                    Comme à l’échelon national, l’équilibre des salaires reste en faveur du genre Homme et les montants médians sont similaires à 
                    ceux pratiqués dans les campagnes Françaises.  
                    <p><strong>Source : Insee</strong></p>
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("https://i.imgur.com/z6wkgSw.png")

    st.divider()
    # ----------------------------------------------------------------------------------------------------------------------------------------------
    # Section 2
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    st.header("2 – Le Cinéma dans la Creuse")
    st.markdown("**Source : CNC**")

    st.subheader("Emplacements")

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image("https://i.imgur.com/9ZwCxHQ.jpeg")
        st.markdown("""
            <p style="text-align: center; font-size: 14px;">
            <strong>Source : OpenStreetMap</strong>
            </p>
        """, unsafe_allow_html=True)

    st.markdown("""
        <p style="text-align: justify; font-size: 16px;">
        Le département de la Creuse compte 5 cinémas répartis dans des villes différentes.  
        Bien que les années dites « Covid » aient fortement ralenti les fréquentations entre 2021 et 2023, ce service s’est maintenu dans ses activités.
        </p>
    """, unsafe_allow_html=True)

    st.subheader("Activité")

    st.markdown("""
    La fréquentation des cinémas connaît également un déclin, en particulier depuis 2016,  
    mais les données issues du site CNC montrent une modification dans les méthodes de recensement utilisées avant et après 2016 :
    """)

    st.image("https://i.imgur.com/zluoMze.png")

    st.markdown("""
        <p style="text-align: justify; font-size: 16px;">
        Globalement, lorsque la population décroît de 5% entre 2016 et 2023,  
        les fréquentations sont en baisse de 18%, révélant que le simple déclin démographique n’explique pas cette baisse à lui seul.
        </p>
        <p style="text-align: justify; font-size: 16px;">
        L’événement COVID est visible sur les années 2021 à 2023 et a mis un frein à une reprise des fréquentations.  
        Néanmoins, cette reprise semble réapparaître en 2023.
        </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.image("https://i.imgur.com/Qv3AdYr.png")

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 300px;">
                <p style="text-align: justify; font-size: 16px;">
                Le Sénéchal est le plus important cinéma de la Creuse,  
                loin devant les autres en matière de chiffre d’affaires (estimés) et de fréquentation.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    📊 **Fréquentation selon les jours :**  
    - **Week-end** : fréquentation maximale  
    - **Mercredi** : jour ouvré le plus fréquenté  
    - COVID a lissé la fréquentation (2021–2022)
    """)

    st.image("https://i.imgur.com/MOgzRfh.png")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.image("https://i.imgur.com/JNGU5Yz.png")

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 310px;">
                <p style="text-align: justify; font-size: 16px;">
                Sur l'ensemble de la période, il existe un transfert d'entrée des jours ouvrés vers le week-end.  
                Le week-end possède également son propre panel de visiteurs.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("Le public")

    st.markdown("""
    👥 **Catégories les plus présentes :**  
    1. **+50 ans**  
    2. 15–24 ans  
    3. 35–49 ans

    📉 Toutes les catégories sont en baisse globale, malgré quelques années de rebond.
    """)

    st.image("https://i.imgur.com/TMBu4J0.png")

    st.subheader("Les genres de film préférés")

    st.markdown("""
    🎭 **Top genres (global)** :  
    - **Comédies** (24%)  
    - **Action** & **Thrillers** (16%)

    🎯 **Par sexe :**  
    - Femmes : Comédies (28%), Thrillers (18%)  
    - Hommes : Action (21%), Comédies (20%)

    🎯 **Par tranche d’âge :**  
    - **18–24 ans** : Comédies (21%), Action (20%), Comédies romantiques & fantastiques (17%)  
    - **25–34 ans** : moins investis, sauf Comédies (22%)  
    - **35–49 ans** : Comédies (26%), Action (16%), Thrillers  
    - **50–64 ans** : Comédies et Action (21%), Thrillers (18%)  
    - **65+ ans** : Comédies (29%), Thrillers  
    **Source : CSA**
    """)

    st.image("https://i.imgur.com/s23ZB6D.png")

    st.subheader("La VOD")

    st.markdown("""
    📺 Le développement de la VOD fragilise les cinémas depuis les années 2010.  
    La crise COVID a accéléré ce phénomène :  
    - De nombreux films ont été produits directement pour les plateformes  
    - En France : 10–15% des films ont basculé vers la VOD  
    **Source : cairn.info**
    """)

    st.divider()

    # ----------------------------------------------------------------------------------------------------------------------------------------------
    # Section 3
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    st.header("Conclusion")
    st.markdown("""
    - La **Creuse** reste l’un des départements les moins peuplés, avec une population en déclin  
    - L’agriculture domine l’économie, mais le chômage reste élevé  
    - Le **cinéma intéresse encore** certains profils, surtout les +50 ans  
    - Le segment 25–49 ans est sous-exploité, mais plein de potentiel  
    - La VOD et la crise COVID ont affaibli durablement la fréquentation  
    - Un service de cinéma moderne devra intégrer :
      - Une riche offre **comédies/action/thrillers**
      - Un **profilage utilisateur** intelligent pour adapter les propositions
    """)

with onglets[2]:
    #st.header("📈 Statistiques et Machine Learning")
    data = "https://github.com/SwingBox/Projet_2/blob/Karim/Movies.csv"
    df = pd.read_csv(data,sep = '\t', low_memory=False)

    columns = ['category','primaryName','ordering','genres','characters','production_companies_name']

    for column in columns:
        df[column] = df[column].str.replace('[','')
        df[column] = df[column].str.replace(']','')
        df[column] = df[column].str.replace("'","")
        df[column] = df[column].str.replace(', ',',')
        df[column] = df[column].astype(str).apply(lambda x: x.split(','))
        
    df['actors'] = df.apply(lambda row: [name for name, cat in zip(row['primaryName'], row['category']) if cat in ['actor', 'actress']], axis=1)
    df['directors'] = df.apply(lambda row: [name for name, cat in zip(row['primaryName'], row['category']) if cat in ['director']], axis=1)

    def doublons(liste):
        liste_finale =[]
        for i in range(len(liste)):
            if liste[i] not in liste_finale:
                liste_finale.append(liste[i])
        return liste_finale

    df['actors'] = df['actors'].apply(lambda x: doublons(x))

    df['leading_role'] = df['actors'].apply(lambda x: str(x[0]) if isinstance(x, list) and len(x) > 0 else r'\N')
    df['second_role'] = df['actors'].apply(lambda x: str(x[1]) if isinstance(x, list) and len(x) > 1 else r'\N')
    df['third_role'] = df['actors'].apply(lambda x: str(x[2]) if isinstance(x, list) and len(x) > 2 else r'\N')
    df['leading_director'] = df['directors'].apply(lambda x: str(x[0]) if isinstance(x, list) and len(x) > 0 else r'\N')

    df = df.loc[df['third_role'] != r'\N']
    df = df.loc[df['leading_director'] != r'\N']

    st.markdown("<h1 style='text-align: center;'>STATISTIQUES SUR LA BASE DE DONNEES MOVIES</h1>", unsafe_allow_html=True)


    # ----------------------------------------------------------------------------------------------------------------------------------------------
    # Section 1
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    st.header("1 – Nombre de films par genre")

    fig = px.histogram(df,x = 'genres1', height = 500, width = 700, title = 'Nombre de film par premier genre - Movies')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Très clairement, le nombre de films du genre Drama se démarque et représente 37% de la base de donnée, suivi du genre Comedy, puis Action.
                <p>Ce déséquilibre sera problématique lors de la phase de Machine Learning et il faudra s'adapter ou faire des concessions.
                <p>
                <p>La distribution des films par second genre laisse apparaître les 'antislash N' avec 2100 unités, nous retrouvons 
                quasiment autant de films du genre Drama, puis Romance avec tout juste 1000 unités :
                </p>
            """, unsafe_allow_html=True)

    fig1 = px.histogram(df,'genres2', height = 500, width = 700, title = 'Nombre de film par second genre')
    fig1.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig1, use_container_width=True)

    # *********************************

    st.header("2 – Popularité moyenne par genre")

    df_genres_pop = df[['genres1','popularity']]
    df_genres_pop = df_genres_pop.groupby('genres1').agg('mean').sort_values('popularity',ascending = False).reset_index()
    df_genres_pop['popularity'] = df_genres_pop['popularity'].apply(lambda x: round(x, 1))

    fig4 = px.bar(df_genres_pop,'genres1','popularity', width=1000, title = 'Popularité par genre',color = 'genres1', color_discrete_sequence = px.colors.qualitative.T10, text_auto = True)
    fig4.update_layout(template = None, xaxis = None, legend = dict(title = 'Genre', y = 1),bargap=0.05,bargroupgap=0.02)

    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Très clairement, le nombre de films du genre Drama se démarque et représente 37% de la base de donnée, suivi du genre Comedy, puis Action.
                <p>Ce déséquilibre sera problématique lors de la phase de Machine Learning et il faudra s'adapter ou faire des concessions.
                <p>
                <p>La distribution des films par second genre laisse apparaître les 'antislash N' avec 2100 unités, nous retrouvons 
                quasiment autant de films du genre Drama, puis Romance avec tout juste 1000 unités :
                </p>
            """, unsafe_allow_html=True)

    # *********************************

    st.header("3 – Note moyenne par genre")

    df_genres_avgRating = df[['genres1','averageRating']]
    df_genres_avgRating = df_genres_avgRating.groupby('genres1').agg('mean').sort_values('averageRating',ascending = False).reset_index()
    df_genres_avgRating['averageRating'] = df_genres_avgRating['averageRating'].apply(lambda x: round(x, 1))

    fig5 = px.bar(df_genres_avgRating,'genres1','averageRating', width=1000, title = 'Note moyenne par genre',color = 'genres1', color_discrete_sequence = px.colors.qualitative.T10, text_auto = True)
    fig5.update_layout(template = None, xaxis = None, legend = dict(title = 'Genre', y = 1))

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Les notes ayant fait l'objet d'un filtrage > 6.8, il est naturel de retrouver des moyennes dans une fourchette de donnée très étroites.
                <p>Observons leur répartition et leur distribution :
                </p>
            """, unsafe_allow_html=True)

    fig6 = px.box(df,'averageRating', height = 500, width = 500,title = 'Répartition des notes moyennes')
    fig7 =px.histogram(df,'averageRating', height = 500, width = 500, title = 'Distribution des notes moyennes')

    col1, col2 = st.columns([1,1], gap="large")

    with col1:
        st.plotly_chart(fig6, use_container_width=True)
    with col2:
        st.plotly_chart(fig7, use_container_width=True)
        
    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Avec un 3ème quartile à 7.5, 75% des notes moyennes sont sous ce quartile et nous observons plusieurs outliers.
                <p>La médiane se trouvant à 7.2, nous retrouvons 50% des notes moyennes entre 6.9 et 7.5.
                <p>
                <p>La Distribution des notes moyennes confirme les résultats de la boxplot.
                <p>Ces informations ne joueront pas un rôle crucial dans notre moteur de machine learning.
                </p>
            """, unsafe_allow_html=True)

    # *********************************

    st.header("3 – Budget par genre")
    df_genres_Budget = df[['genres1','budget']]
    df_genres_Budget = df_genres_Budget.groupby('genres1').agg('mean').sort_values('budget',ascending = False).reset_index()

    fig8 = px.bar(df_genres_Budget,'genres1','budget', width=1000, title = 'Budget moyen par genre',color = 'genres1', color_discrete_sequence = px.colors.qualitative.T10)
    fig8.update_layout(template = None, xaxis = None, legend = dict(title = 'Genre', y = 1))

    st.plotly_chart(fig8, use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Les budgets moyens par genre montrent une différence exploitable entre les genres des films. Ces données devraient pouvoir jouer un rôle intéressant dans notre modèle de Machine Learning.
                </p>
            """, unsafe_allow_html=True)
    

with onglets[3]:
    #st.header("🤖Préparation des données et Machine Learning")
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
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Prepa_donnees/Table%20des%20relations.png", use_container_width=True)

    st.markdown("<p><p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,3,1], gap="large")
    with col2:
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Prepa_donnees/D%C3%A9tail%20relations.png", use_container_width=True)

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

    st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Prepa_donnees/Features.png")

    # ------------- ML ------------- #
    # ------------- ML ------------- #
    # ------------- ML ------------- #
    # ------------- ML ------------- #
    # ------------- ML ------------- #
    X_reduced = pd.read_csv('https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/X_final.csv', sep = '\t')

    st.markdown("<h1 style='text-align: center;'>REALISATION DU MOTEUR DE MACHINE LEARNING</h1>", unsafe_allow_html=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                    La phase de machine learning a été une des phases les plus délicates.
                    <p>Etant donné que l'objectif du moteur est la recommandation de film, le ML non supervisé en clustering était le plus préconisé 
                    (affichage des voisins les plus proches de l'input).
                    <p>
                    Nous tenions absolument à ce que les recommandations se rapportent prioritairement au genre du film en input pour éviter que lorsque 
                    l'utilisateur entre le nom d'un film d'action, nous ne lui proposions que des films du genre Romance ou des documentaires.
                    <p>Néanmoins, nous avons noté que les genres figurants dans la base de donnée était défini de manière anglo-saxonne, 
                    ce qui est très différent d'une définition de genre à la Française.
                    Ici se trouve la plus grande contrainte de notre moteur et celle-ci s'est avérée sans solution facile à mettre en oeuvre.
                    <p>Nous traitonbs ici de la phase finale du Machine Learning, avant cetet phase beacoup de tests ont été réalisés et les features transformées, entre autres les 
                    colonnes de liste ont été encodées avec FeaturesHasher(), puis une sélection des colonnes pertinentes a été effectuée en ne sélectionnant que les colonnes qui 
                    nous permettaient d'obtenir le meilleur Silouhette Score du modèle retenu. Sur la phase de test, nous avons utilisé GridSearch() pour évaluer nos modèles
                    et c'est DBScan() qui a offert les meilleurs résultats avec les paramètres optimisés pour l'ensemble des modèles testés (KNN, K-Means, DB-Scan).
                    <p>Nous avons noté que même après un preprocessoring tel que nous le définiront par la suite, la création des clusters fut très difficle, mais nous en reparlerons plus tard.
                </p>
                """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1], gap="large")
    with col2:
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/MachineLearning.jpg")
    
    # ----------------------------------------------------------------------------------------------------------------------------------------------
    # Section 1
    # ----------------------------------------------------------------------------------------------------------------------------------------------

    st.header("1 – Définition des features")

    st.markdown("""
                    <p style="text-align: justify; font-size: 16px;">
                    Voici une première idée de notre feature de départ :
                    </p>
                """, unsafe_allow_html=True)

    st.dataframe(X_reduced.head(), use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                    Le DataFrame initial comporte 10830 lignes et 12 colonnes.
                </p>
                """, unsafe_allow_html=True)

    st.markdown("<p><p>", unsafe_allow_html=True)



    # ***************************

    st.header("2 – Réalisation du préprocessoring")

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Le type des données passant du numérique, à la catégorie en passant par des listes, le préprocessor a été établi en fonction de plusieurs critères.
                    <p>Nous avons alors identifié le nombres d'éléments uniques par colonne mais aussi le type de colonne et le type précis des valeurs :
                </p>
                """, unsafe_allow_html=True)

    df_uniques = pd.DataFrame({
        'Colonnes': X_reduced.columns,
        'Nombre de termes uniques': [
                X_reduced[column].explode().nunique()
                if X_reduced[column].apply(lambda x: isinstance(x, list)).any() else X_reduced[column].nunique() 
                for column in X_reduced.columns
                                    ],
        'Dtypes': [str(X_reduced[column].dtype) for column in X_reduced.columns],
        'xtypes': X_reduced.apply(lambda col: ', '.join(col.dropna().apply(lambda x: type(x).__name__).unique()), axis=0),
                                },
        index=X_reduced.columns).sort_values(['Dtypes','xtypes']).reset_index().drop('index', axis=1)

    st.dataframe(df_uniques, use_container_width=True)

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                    A partir de ces informations, nous avons pu sélectionner les modèles à intégrer au preprocessoring des données 
                    (après avoir réalisé un premier preprocessoring avec FeatureHasher) :
                    <p>1.  StandardScaler() : données numériques.
                    <p>2.  OneHotEncoder() : données catégorielles avec faible nombre d'uniques (colonne genres1 uniquement).
                    <p>3.  BinaryEncoder() : données catégorielles avec nombre important d'uniques (oveviewNLP, colonnes des acteurs et directeurs).
                    <p>
                    <p>En phase de test, les données, même après preprocessoring avec ces modèles restaient difficilement discernables pour les modèles de clustering.
                    Nous avons alors, après preprocessoring, ajouté un nouveau tranformateur : PCA() - Component Principal Analysis, qui réduit la dimensionnalité des données correlées
                    en vecteurs non corrélés en "capturant" le maximum de variance pour créer ses composantes principales (les n_components).
                </p>
                """, unsafe_allow_html=True)

    # ***************************

    st.header("3 – Réalisation du moteur final")

    st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Une fois le double preprocessoring réalisé, DB-Scan est entré en action. Avec ses paramètres optimisés, le nombre de clusters optimal était de 31 clusters.
                Ces clusters contenaient tous les genres de film, ce qui n'allait pas dans le sens de notre objectif de groupe, il fallait alors trouver un moyen de garder le résultat de DB-Scan, mais de forcer le genre des films sur une correspondance exacte,
                dans la mesure du possible, à l'imput.
                <p>Nous avons alors intégré un outil supplémentaire, cosine_similarity, qui fonctionne sur la distance avec les voisins les plus proches, comme le fait KNN et DB-Scan,
                mais de manière plus simple et rapide. Cosine_similarity prend le relais sur DB-Scan lorsque DB-scan indentifie un input comme du bruit (classé -1 en cluster).
                Dans notre DataFrame de features, 189 films sont classés en "bruit", c'est à dire qu'ils sont en périphérie des clusters et donc ne leurs appartiennent pas (epsilon optimal pour nos features = 1).
                    <p>En conclusion, notre fonction intervient en trois parties :
                    <p>1.  Double preprocessoring (pour ne pas dire triple avec FeatureHasher).
                    <p>2.  Clustering avec DB-Scan.
                    <p>3.  Filtrage de la matrice PCA sur le genre et récupération des index de films dont la distance est la plus proche de l'input.
                    <p>4.  Récupération des index dans le DataFrame servant de base de données pour obtenir le titre des films recommandés.
                    <p>5.  En cas d'input clustérisé en tant que bruit, prise du relais par Cosine_similarity.
                    <p>6.  Renvoi des titres de films recommandés.
                <p>Pour finir, une autres méthodologie a été testée mettant en jeu uniquement la colonne 'overview', sur laquelle a été appliquée TfIdf (ajout d'une colonne ne contenant sur les mots-clefs par genre)
                après l'avoir nettoyée grâce à StopWords, mais le temps à manqué pour aller au bout de ce test.
                </p>
                """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1], gap="large")
    with col2:
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/output.png")

    st.markdown("<h1 style='text-align: center;'>TO BE CONTINUED ...</h1>", unsafe_allow_html=True)
    st.markdown("<p><p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1], gap="large")
    with col2:
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/cluster_distance.png")
    st.markdown("<p><p>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/clusterdistance.png")
    st.markdown("<p><p>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/silhouette.png")
    st.markdown("<p><p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1], gap="large")
    with col2:
        st.image("https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Machine_Learning/clusters.png")





with onglets[4]:
    st.header("👥 L'équipe projet")
    st.markdown("Rencontrez les membres passionnés derrière **CreuzFlix** :")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("https://i.imgur.com/7OK5LB4.png", width=180)
        st.subheader("🧠 Karim")
        st.markdown("Audacieux, sérieux, maître incontesté du machine learning.")

    with col2:
        st.image("https://i.imgur.com/xjkQgng.png", width=180)
        st.subheader("👨‍💻 Asseguerem")
        st.markdown("Curieux, vigilant, padawan de la Data et de la gestion de projet.")

    with col3:
        st.image("https://i.imgur.com/EeXfKXb.png", width=180)
        st.subheader("🐆 Grace")
        st.markdown("La légende raconte que c'est elle qui a découvert la Creuse lors d'une expédition maritime.")

    with col4:
        st.image("https://i.imgur.com/2lmsWdp.png", width=180)
        st.subheader("🦆 Nathan")
        st.markdown("Souple, élégant, pourfendeur de Streamlit.")

with onglets[5]:
    st.header("✅ Conclusion et perspectives")
    st.markdown("""
    L'application Creuzflix pose les bases d'une plateforme de recommandation de films personnalisée.  
    Des évolutions futures peuvent inclure la connexion utilisateur, la sauvegarde des préférences, et des recommandations en temps réel via API.
    """)
