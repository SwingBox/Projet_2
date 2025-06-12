import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from category_encoders import BinaryEncoder
from sklearn.metrics import  make_scorer,precision_score
from sklearn.metrics import accuracy_score, f1_score, recall_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid

from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import  make_scorer,precision_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import ndcg_score

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

X_reduced = pd.read_csv('https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/X_final.csv', sep = '\t')

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ['production_companies_name_hash_0','directors_hash_1','genres_hash_0','genres_hash_1','genres_hash_2',]),
    ("cat_ohe", OneHotEncoder(), ['genres1',]),
    ("cat_bin", BinaryEncoder(), ['overviewNLP','leading_role','second_role','third_role','leading_director','Title']),
])

def recommend_movies_dbscan(movie_title, n_recommendations=10):
    """Recommande des films similaires basés sur DBScan et ajuste si nécessaire."""
    X_transformed = preprocessor.fit_transform(X_reduced)
    X_pca = PCA(n_components=5).fit_transform(X_transformed)
    # Index du film recherché ([0] car plusieurs films du même titre)
    movie_index = X_reduced[X_reduced['Title'] == movie_title].index[0]
    
    # Evaluation DBScan
    dbscan = DBSCAN(eps=1, min_samples=10)
    labels_dbscan = dbscan.fit_predict(X_pca)

    # Identification du cluster du film recherché
    cluster_id = labels_dbscan[movie_index]

    if cluster_id == -1:
        print(f"🚨 `{movie_title}` est classé comme bruit par DBScan. Bascule sur Cosine Similarity.")
        return refine_with_cosine(movie_title, n_recommendations)

    # Extraction des films du même cluster
    cluster_movies_idx = [i for i, label in enumerate(labels_dbscan) if label == cluster_id]
    recommended_movies = X_reduced.iloc[cluster_movies_idx][['Title','genres1']]

    # Vérification de la cohérence des genres
    movie_genre = X_reduced.iloc[movie_index]['genres1']
    genre_match = recommended_movies[X_reduced['genres1'] == movie_genre]

    if len(genre_match) > 0:
        # Affichage des recommandations
        print(f"🎬 **Films similaires à {movie_title} et du même genre, via DBScan:**")
        return genre_match.drop(movie_index).head(10)
    else:
        print(f"⚠️ Les films recommandés par DBScan sont dispersés. Résultat du filtrage par genre + Cosine Similarity.")
        return refine_with_cosine(movie_title, n_recommendations=10)

def refine_with_cosine(movie_title, n_recommendations=10):
    """Affiner les recommandations avec Cosine Similarity."""
    X_transformed = preprocessor.fit_transform(X_reduced)
    X_pca = PCA(n_components=5).fit_transform(X_transformed)
    # Trouver l’index du film recherché
    movie_index = X_reduced[X_reduced['Title'] == movie_title].index[0]
    
    # Filtrage sur le genre recherché
    movie_genre = X_reduced.iloc[movie_index]['genres1']
    genre_filtered = X_reduced[X_reduced['genres1'] == movie_genre]
    X_filtered = X_pca[genre_filtered.index]

    # Calcul de la similarité cosinus
    similarities = cosine_similarity(X_filtered)
    similar_movies_idx = similarities[movie_index].argsort()[::-1][1:n_recommendations+1]

    # Affichage des recommandations affinées
    return genre_filtered.iloc[similar_movies_idx][['Title', 'genres1']].head(10)
