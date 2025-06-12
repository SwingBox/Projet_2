import streamlit as st
import pandas as pd
import numpy as np

# Import des bibliothèques de viz
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = "https://raw.githubusercontent.com/SwingBox/Projet_2/refs/heads/Karim/Movies.csv"
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

st.set_page_config(page_title="Statistiques de la base de données", layout="wide")
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
fig4.update_layout(template = None, xaxis = None, legend = dict(title = 'Genre', y = 1))

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
