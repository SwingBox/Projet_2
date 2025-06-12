import streamlit as st
import pandas as pd
import numpy as np

X_reduced = pd.read_csv('https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/X_final.csv', sep = '\t')

st.set_page_config(page_title="Réalisation du moteur de Machine Learning", layout="wide")
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
st.image("./MachineLearning.jpg", use_container_width=True)
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

st.image("./output.png", use_container_width=True)

st.markdown("<h1 style='text-align: center;'>TO BE CONTINUED ...</h1>", unsafe_allow_html=True)
st.markdown("<p><p>", unsafe_allow_html=True)
st.image("./cluster_distance.png", use_container_width=True)
st.markdown("<p><p>", unsafe_allow_html=True)
st.image("./clusterdistance.png", use_container_width=True)
st.markdown("<p><p>", unsafe_allow_html=True)
st.image("./silhouette.png", use_container_width=True)
st.markdown("<p><p>", unsafe_allow_html=True)
st.image("./clusters.png", use_container_width=True)
