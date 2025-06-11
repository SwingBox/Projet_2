import streamlit as st

st.set_page_config(page_title="Étude Cinéma - Creuse", layout="wide")
st.markdown("<h1 style='text-align: center;'>ETUDE DEMOGRAPHIQUE ET SECTORIELLE</h1>", unsafe_allow_html=True)
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
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Creuse.png", use_container_width=True)  # Correction ici

with col2:
    # Ajout du texte avec hauteur adaptée pour s'aligner avec l'image
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 400px;">
            <p style="text-align: justify; font-size: 16px;">Originaire de la province de la Marche, c’est le 4 mars 1790 que fût créé par la Révolution Française le département de la Creuse (23).
            Il est un département Français dont le nom vient du fleuve de la Creuse, affluent de la Vienne et est encore aujourd’hui le 2ème plus petit département Français par sa population avec
            <strong>114 103 habitants estimés en 2025</strong> (0.17% de la population Française).</p>
            <p style="text-align: center; font-weight: bold;">Sources : Wikipédia – Insee.</p>
        </div>
    """, unsafe_allow_html=True)

# ***************************

st.subheader("La population")

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Evolution Population Creuse vs France.png")

with col2:
    st.markdown("""
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 500px;">
                    <p style="text-align: justify; font-size: 16px;">
                    À l’inverse de la population française, la population de la Creuse est en déclin depuis le 19è siècle (287 000 habitants) 
                    en raison du solde naturel négatif (balance natalité – mortalité), bien que légèrement amortie par le solde migratoire (+350 hab/an).  
                    En 2021, la population active reste majoritaire, bien que les <strong>60-74 ans</strong> prédominent en nombre. 
                    Le <strong>genre féminin</strong> est aussi légèrement plus représenté, surtout après 65 ans.  
                    <P><strong>Source : Insee</strong></p>
                    </p>
                </div>
                """, unsafe_allow_html=True)
st.markdown("""En 2021, la population active reste majoritaire, bien que les **60-74 ans** prédominent en nombre. Le **genre féminin** est aussi légèrement 
            plus représenté, surtout après 65 ans.  
                    **Source : Insee**""")
st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Population par tranches d'âge.png")

# ***************************

st.subheader("L’économie")

st.markdown("""
L’agriculture est la principale source économique dans la Creuse. En 2013 :  
- Agriculture : **11,9%** de l’emploi total (seul le Gers fait mieux avec 12.2%)  
- Industrie : **10,7%**  
- Construction : **6,5%**
            """)

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Catégories SocioProfessionnelles.png")

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
    
st.markdown("<p><p>", unsafe_allow_html=True)

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
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Salaires par Cat SocPro.png")

st.divider()

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Section 2
# ----------------------------------------------------------------------------------------------------------------------------------------------

st.header("2 – Le Cinéma dans la Creuse")
st.markdown("**Source : CNC**")

st.subheader("Emplacements")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Cinemas Creuse.jpeg")
    st.markdown("""
                    <p style="text-align: center; font-size: 14px;">
                    <strong>Source : OpenStreetMap</strong>
                    </p>
            """, unsafe_allow_html=True)

st.markdown("""
                <p style="text-align: justify; font-size: 16px;">
                Le département de la Creuse compte 5 Cinémas répartis dans des villes différentes. Bien que les années dites « Covid » ont fortement ralentis les fréquentations entre 2021 et 2023, ce service s’est maintenu dans ses activités
                </p>
            """, unsafe_allow_html=True)

# ***************************

st.subheader("Activité")

st.markdown("""
La fréquentation des Cinémas connaît également un déclin, en particulier depuis 2016, mais les données issues du site CNC montre une modification dans les méthodes de recensement utilisées avant et après 2016 :
""")
st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Evolution Population et Fréquentation.png")

st.markdown("""
            <p style="text-align: justify; font-size: 16px;">
            Globalement, lorsque la population décroît de 5% entre 2016 et 2023, les fréquentations sont en baisse de 18%, 
            révélant que le simple déclin démographique n’explique pas cette baisse à lui seul.
            </p>
            <p style="text-align: justify; font-size: 16px;">
            L’événement COVID est visible sur les années 2021 à 2023 et a mis un frein à une reprise des fréquentations en 2021, 
            néanmoins cette reprise semble réapparaître en 2023.
            </p>
            """, unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Cinémas CA et entrées.png")

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
st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Fréquentation Jours Semaine.png")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Heatmap Fréquentation Jours Semaine.png")

with col2:
    st.markdown("""
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 310px;">
                    <p style="text-align: justify; font-size: 16px;">
                    Sur l'ensemble de la période, il existe un transfert d'entrée des jours ouvrés vers le week-end, 
                    un peu moins entre les jours de la semaine travaillés, mais le week-end possède également son propre panel de visiteurs.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# ***************************

st.subheader("Le public")
st.markdown("""
👥 **Catégories les plus présentes :**  
1. **+50 ans**  
2. 15–24 ans  
3. 35–49 ans

📉 Toutes les catégories sont en baisse globale, malgré quelques années de rebond.
""")
st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Public selon âge.png")

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
st.image("/Users/kdahm/Desktop/Formation_DATA_Analyst/Projet_2/Graphiques/Plotly/Genres préférés sexe et âge.png")

# ***************************

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
