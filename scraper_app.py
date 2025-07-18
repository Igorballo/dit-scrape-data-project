import streamlit as st
import pandas as pd
import numpy as np
import base64
import plotly.express as px
from scraping_functions import scrape_motos_data, scrape_voitures_data, scrape_location_data


# Configuration de la page
st.set_page_config(
    page_title="Plateforme de Scraping - Expat Dakar",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour une meilleure apparence
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: white;
        padding: 1.3rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation des variables de session
if 'scraped_data' not in st.session_state:
    st.session_state.scraped_data = pd.DataFrame()
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Accueil"

# Fonction pour télécharger un fichier CSV
def download_csv(dataframe, filename):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv" class="download-link">📥 Télécharger {filename}</a>'
    return href


# Fonction pour nettoyer les données
def clean_data(dataframe):
    """Fonction pour nettoyer les données scrapées"""
    if dataframe.empty:
        return dataframe
    
    # Copie des données
    df_clean = dataframe.copy()

    # Je veux drop certaine colonne ici
    df_clean.drop(columns=['web-scraper-order', 'web-scraper-start-url', 'containers_links','containers_links-href'], inplace=True)

    print("igor",df_clean)

    # Nettoyer le prix
    df_clean["prix_numerique"] = df_clean["prix"].str.replace(r"[^\d]", "", regex=True)
    df_clean["prix_numerique"] = pd.to_numeric(df_clean["prix_numerique"], errors='coerce')

    # Nettoyer l'année
    df_clean["annee_numerique"] = df_clean["annee"].str.extract(r"(\d{4})")
    df_clean["annee_numerique"] = pd.to_numeric(df_clean["annee_numerique"], errors='coerce')

    # Nettoyer le kilométrage
    df_clean["kilometrage_numerique"] = df_clean["kilometrage"].str.replace(r"[^\d-]", "", regex=True)
    df_clean["kilometrage_numerique"] = pd.to_numeric(df_clean["kilometrage_numerique"], errors='coerce')
    
    # Traitement des valeurs négatives
    df_clean.loc[df_clean["kilometrage_numerique"] < 0, "kilometrage_numerique"] = np.nan
    

    return df_clean


# Page d'accueil
def show_home():
    st.markdown("""
    <div class="main-header">
        <h1>Plateforme de Scraping - Expat Dakar</h1>
        <p>Votre solution complète pour la collecte et l'analyse de données automobiles</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Notre Mission</h3>
        <span>Cette plateforme vous permet de collecter, analyser et télécharger des données automobiles 
        depuis Expat-Dakar de manière simple et efficace. Que vous soyez un particulier cherchant 
        une moto ou un analyste de données, cette plateforme vous accompagne dans votre démarche.</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🕷️ Scraping Intelligent</h4>
            <span>Collectez automatiquement les données de plusieurs pages avec notre outil de scraping avancé.</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Dashboard</h4>
            <span>Visualisez vos données avec des graphiques interactifs et des métriques clés.</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📥 Téléchargement Facile</h4>
            <span>Téléchargez vos données au format CSV pour une utilisation ultérieure.</span>
        </div>
        """, unsafe_allow_html=True)

# Page de scraping
def show_scraping():
    st.markdown("<h2>🕷️ Scraping de Données</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span>Configurez vos paramètres de scraping et lancez la collecte de données depuis Expat-Dakar.</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Configuration")
        url = st.selectbox("URL de base", options=["https://dakar-auto.com/senegal/voitures-4", "https://dakar-auto.com/senegal/motos-and-scooters-3", "https://dakar-auto.com/senegal/location-de-voitures-19"], index=0)
        
        max_pages = st.number_input("Nombre de pages à scraper", value=1, min_value=1, step=1)
        
        if st.button("🚀 Lancer le Scraping", key="scrape_btn"):
            if url and url == 'https://dakar-auto.com/senegal/voitures-4':
                scraped_df = scrape_voitures_data(max_pages)
                st.session_state.scraped_data = scraped_df
            elif url and url == 'https://dakar-auto.com/senegal/motos-and-scooters-3':
                scraped_df = scrape_motos_data(max_pages)
                st.session_state.scraped_data = scraped_df
            elif url and url == 'https://dakar-auto.com/senegal/location-de-voitures-19':
                scraped_df = scrape_location_data(max_pages)
                st.session_state.scraped_data = scraped_df
            else:
                st.error("Veuillez entrer une URL valide.")
    
    with col2:
        st.subheader("Données Scrapées")
        if hasattr(st.session_state, 'scraped_data') and not st.session_state.scraped_data.empty:
            # Afficher toutes les données sans limite
            st.dataframe(st.session_state.scraped_data, use_container_width=True)
            
            # Afficher le nombre total de données
            st.write(f"**Total des données scrapées : {len(st.session_state.scraped_data)} lignes et {len(st.session_state.scraped_data.columns)} colonnes**")
            
            # Bouton de téléchargement
            csv_link = download_csv(st.session_state.scraped_data, "donnees_scrapees")
            st.markdown(csv_link, unsafe_allow_html=True)
        else:
            st.info("Aucune donnée scrapée pour le moment. Lancez le scraping pour commencer.")

# Page de téléchargement
def show_download():
    st.markdown("<h2>📥 Téléchargement de Données</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span>Téléchargez les données déjà scrapées et stockées dans notre base de données.</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des fichiers disponibles
    available_files = [
        ('dakar-location-voitures-sitemap.csv', 'https://dakar-auto.com/senegal/location-de-voitures-19'),
        ('motos-scooters-sitemap.csv', 'https://dakar-auto.com/senegal/motos-and-scooters-3'),
        ('dakar-voiture-2753-sitemap.csv', 'https://dakar-auto.com/senegal/voitures-4'),
    ]
    
    st.subheader("Fichiers Disponibles")
    
    for filename, description in available_files:
        try:
            df = pd.read_csv(f'data/{filename}')
            
            col1, col2, col3, col4 = st.columns([3, 1, 1, 2])
            
            with col1:
                st.write(f"**{description}**")
            
            with col2:
                st.write(f"📊 {df.shape[0]} lignes")
            
            with col3:
                st.write(f"📋 {df.shape[1]} colonnes")
            
            with col4:
                csv_link = download_csv(df, filename)
                st.markdown(csv_link, unsafe_allow_html=True)
            
            st.divider()
            
        except FileNotFoundError:
            st.warning(f"Fichier {filename} non trouvé.")
    

# Page dashboard
def show_dashboard():
    st.markdown("<h2>📊 Dashboard Analytique</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span>Visualisez et analysez vos données avec des graphiques interactifs et des métriques clés.</span>
    </div>
    """, unsafe_allow_html=True)

    try:
        # Charger le CSV
        df = pd.read_csv("data/data_to_analyse.csv")
        
        # Nettoyage des données pour le dashboard
        df_clean = clean_data(df)
        
        # Supprimer les lignes avec des données manquantes pour les métriques
        df_metrics = df_clean.dropna(subset=['prix_numerique', 'annee_numerique', 'kilometrage_numerique'])
        
        if df_metrics.empty:
            st.warning("Aucune donnée valide à afficher dans le dashboard.")
            return
        
        # Métriques principales
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Nombre total", len(df_metrics))
        
        with col2:
            avg_price = df_metrics['prix_numerique'].mean()
            st.metric("Prix moyen", f"{avg_price:,.0f} FCFA")
          
        with col3:
            avg_km = df_metrics['kilometrage_numerique'].mean()
            st.metric("Km moyen", f"{avg_km:,.0f} km")
        
        st.markdown("---")
        
        # Graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribution des carburants
            carburant_counts = df_metrics['carburant'].value_counts()
            fig_carburant = px.pie(values=carburant_counts.values, names=carburant_counts.index,
                                  title='Répartition par Type de Carburant')
            st.plotly_chart(fig_carburant, use_container_width=True)
        
        with col2:
            # Distribution des années
            year_counts = df_metrics['annee_numerique'].value_counts().sort_index()
            fig_year = px.bar(x=year_counts.index, y=year_counts.values,
                             title='Distribution par Année',
                             labels={'x': 'Année', 'y': 'Nombre de voitures'})
            st.plotly_chart(fig_year, use_container_width=True)
        
        # Deuxième ligne de graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            # Prix vs Kilométrage
            fig_scatter = px.scatter(df_metrics, x='kilometrage_numerique', y='prix_numerique',
                                    title='Relation Prix vs Kilométrage',
                                    labels={'kilometrage_numerique': 'Kilométrage (km)', 'prix_numerique': 'Prix (FCFA)'})
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Distribution des boîtes de vitesse
            boite_counts = df_metrics['boite_vitesse'].value_counts()
            fig_boite = px.pie(values=boite_counts.values, names=boite_counts.index,
                              title='Répartition par Type de Boîte de Vitesse')
            st.plotly_chart(fig_boite, use_container_width=True)
        
    
    except FileNotFoundError:
        st.error("Fichier 'data/data_to_analyse.csv' non trouvé. Veuillez d'abord scraper des données.")
    except Exception as e:
        st.error(f"Erreur lors du chargement du dashboard: {str(e)}")
        st.info("Assurez-vous que le fichier CSV contient les colonnes attendues.")


# Page formulaire d'évaluation
def show_feedback():
    st.markdown("<h2>📝 Évaluation de l'Application</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span>Aidez-nous à améliorer notre plateforme en partageant votre expérience utilisateur. 
        Utilisez le formulaire ci-dessous pour nous donner votre avis.</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Intégration du formulaire KoboToolbox
    st.markdown("""
    <div style="display: flex; justify-content: center; margin: 2rem 0;">
        <iframe src="https://ee.kobotoolbox.org/i/ei4b3hxS" 
                width="100%" 
                height="700" 
                frameborder="0" 
                style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        </iframe>
    </div>
    """, unsafe_allow_html=True)

# Navigation principale
def main():
    # Sidebar pour la navigation
    st.sidebar.markdown("""
    <div style="text-align: left; padding: 1rem; text-transform: uppercase;">
        <h3>Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Boutons de navigation
    if st.sidebar.button("🏠 Accueil", key="nav_home"):
        st.session_state.current_page = "Accueil"
    
    if st.sidebar.button("🕷️ Scraping", key="nav_scraping"):
        st.session_state.current_page = "Scraping"
    
    if st.sidebar.button("📥 Téléchargement", key="nav_download"):
        st.session_state.current_page = "Téléchargement"
    
    if st.sidebar.button("📊 Dashboard", key="nav_dashboard"):
        st.session_state.current_page = "Dashboard"
    
    if st.sidebar.button("📝 Évaluation", key="nav_feedback"):
        st.session_state.current_page = "Évaluation"
    
    st.sidebar.markdown("---")
    
    # Informations sur l'application
    st.sidebar.markdown("""
    <div style="padding: 1rem;">
        <h4>ℹ️ À propos</h4>
        <p>Plateforme de scraping et d'analyse de données automobiles.</p>
        <p><strong>Version:</strong> 1.0</p>
        <p><strong>Source:</strong> Expat-Dakar</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage de la page sélectionnée
    if st.session_state.current_page == "Accueil":
        show_home()
    elif st.session_state.current_page == "Scraping":
        show_scraping()
    elif st.session_state.current_page == "Téléchargement":
        show_download()
    elif st.session_state.current_page == "Dashboard":
        show_dashboard()
    elif st.session_state.current_page == "Évaluation":
        show_feedback()

if __name__ == "__main__":
    main()




 


