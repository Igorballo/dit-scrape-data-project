import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import base64
import io
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By 


# Instantier l'objet chrome options
options = webdriver.ChromeOptions() 
# définir l'option d'utiliser chrome en mode headless ( utiliser afin de lancer le script en background)
options.add_argument("--headless=new") 
# initialiser l'instance de chrome driver en mode headless
driver = webdriver.Chrome(options=options)


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
        padding: 1.5rem;
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
        padding: 0.75rem 2rem;
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
    st.session_state.scraped_data = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Accueil"

# Fonction pour télécharger un fichier CSV
def download_csv(dataframe, filename):
    csv = dataframe.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv" class="download-link">📥 Télécharger {filename}</a>'
    return href

# Fonction de scraping (exemple pour motos)
def scrape_motos_data(url, max_pages=5):
    """Fonction de scraping pour les données de motos"""
    scraped_data = []
    
    with st.spinner(f'Scraping en cours... Veuillez patienter...'):
        for page in range(1, max_pages + 1):
            try:
                # Simulation de scraping (remplacez par votre logique réelle)
                page_url = f"{url}?page={page}"
                
                # Simulation de données scrapées
                for i in range(10):
                    scraped_data.append({
                        'Titre': f'Moto {page}-{i+1}',
                        'Prix': f'{50000 + (page * 1000) + (i * 500)} FCFA',
                        'Marque': f'Marque {i % 5 + 1}',
                        'Année': f'{2015 + (i % 8)}',
                        'Kilométrage': f'{10000 + (i * 5000)} km',
                        'Localisation': 'Dakar',
                        'Date_Scraping': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                
                # Barre de progression
                progress = page / max_pages
                st.progress(progress)
                time.sleep(0.5)  # Simulation du temps de scraping
                
            except Exception as e:
                st.error(f"Erreur lors du scraping de la page {page}: {str(e)}")
                break

    return pd.DataFrame(scraped_data)

def scrape_voitures_data(url, max_pages):
    """Fonction de scraping pour les données de voitures"""
    scraped_data = []
    
    print(f"Scraping voitures: {url}")
    with st.spinner(f'Scraping voitures en cours... Veuillez patienter...'):
        for page in range(1, max_pages + 1):
            try:
                # Simulation de scraping pour voitures
                page_url = f"{url}?page={page}"
                
                # Simulation de données scrapées
                for i in range(10):
                    scraped_data.append({
                        'Titre': f'Voiture {page}-{i+1}',
                        'Prix': f'{2000000 + (page * 50000) + (i * 25000)} FCFA',
                        'Marque': f'Marque {i % 8 + 1}',
                        'Année': f'{2010 + (i % 12)}',
                        'Kilométrage': f'{50000 + (i * 10000)} km',
                        'Localisation': 'Dakar',
                        'Date_Scraping': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                
                # Barre de progression
                progress = page / max_pages
                st.progress(progress)
                time.sleep(0.5)  # Simulation du temps de scraping
                
            except Exception as e:
                st.error(f"Erreur lors du scraping de la page {page}: {str(e)}")
                break

    return pd.DataFrame(scraped_data)

def scrape_location_data(url, max_pages):
    """Fonction de scraping pour les données de location de voitures"""
    scraped_data = []
    
    print(f"Scraping location: {url}")
    with st.spinner(f'Scraping location en cours... Veuillez patienter...'):
        for page in range(1, max_pages + 1):
            try:
                # Simulation de scraping pour location
                page_url = f"{url}?page={page}"
                
                # Simulation de données scrapées
                for i in range(10):
                    scraped_data.append({
                        'Titre': f'Location {page}-{i+1}',
                        'Prix': f'{15000 + (page * 1000) + (i * 500)} FCFA/jour',
                        'Marque': f'Marque {i % 6 + 1}',
                        'Année': f'{2015 + (i % 8)}',
                        'Kilométrage': f'{80000 + (i * 15000)} km',
                        'Localisation': 'Dakar',
                        'Date_Scraping': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                
                # Barre de progression
                progress = page / max_pages
                st.progress(progress)
                time.sleep(0.5)  # Simulation du temps de scraping
                
            except Exception as e:
                st.error(f"Erreur lors du scraping de la page {page}: {str(e)}")
                break

    return pd.DataFrame(scraped_data)


# Fonction pour nettoyer les données
def clean_data(dataframe):
    """Fonction pour nettoyer les données scrapées"""
    if dataframe.empty:
        return dataframe
    
    # Copie des données
    df_clean = dataframe.copy()
    
    # Nettoyage des prix (suppression de 'FCFA' et conversion en numérique)
    df_clean['Prix_Numerique'] = df_clean['Prix'].str.replace(' FCFA', '').str.replace(' ', '').astype(float)
    
    # Nettoyage du kilométrage
    df_clean['Kilometrage_Numerique'] = df_clean['Kilométrage'].str.replace(' km', '').str.replace(' ', '').astype(float)
    
    # Conversion de l'année en numérique
    df_clean['Annee_Numerique'] = df_clean['Année'].astype(int)
    
    return df_clean

# Fonction pour créer des visualisations
def create_dashboard(dataframe):
    """Création du dashboard avec des graphiques"""
    if dataframe.empty:
        st.warning("Aucune donnée à afficher dans le dashboard.")
        return
    
    # Nettoyage des données pour le dashboard
    df_clean = clean_data(dataframe)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Nombre total", len(dataframe))
    
    with col2:
        avg_price = df_clean['Prix_Numerique'].mean()
        st.metric("Prix moyen", f"{avg_price:,.0f} FCFA")
    
    with col3:
        avg_year = df_clean['Annee_Numerique'].mean()
        st.metric("Année moyenne", f"{avg_year:.0f}")
    
    with col4:
        avg_km = df_clean['Kilometrage_Numerique'].mean()
        st.metric("Km moyen", f"{avg_km:,.0f} km")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribution des prix
        fig_price = px.histogram(df_clean, x='Prix_Numerique', 
                               title='Distribution des Prix',
                               labels={'Prix_Numerique': 'Prix (FCFA)', 'count': 'Nombre'})
        st.plotly_chart(fig_price, use_container_width=True)
    
    with col2:
        # Distribution des années
        fig_year = px.bar(df_clean['Annee_Numerique'].value_counts().reset_index(),
                         x='index', y='Annee_Numerique',
                         title='Distribution par Année',
                         labels={'index': 'Année', 'Annee_Numerique': 'Nombre'})
        st.plotly_chart(fig_year, use_container_width=True)
    
    # Graphique des marques
    fig_brand = px.pie(df_clean, names='Marque', title='Répartition par Marque')
    st.plotly_chart(fig_brand, use_container_width=True)

# Page d'accueil
def show_home():
    st.markdown("""
    <div class="main-header">
        <h1>🚗 Plateforme de Scraping - Expat Dakar</h1>
        <p>Votre solution complète pour la collecte et l'analyse de données automobiles</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Notre Mission</h3>
        <p>Cette plateforme vous permet de collecter, analyser et télécharger des données automobiles 
        depuis Expat-Dakar de manière simple et efficace. Que vous soyez un particulier cherchant 
        une moto ou un analyste de données, notre outil vous accompagne dans votre démarche.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🕷️ Scraping Intelligent</h4>
            <p>Collectez automatiquement les données de plusieurs pages avec notre outil de scraping avancé.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Dashboard Analytique</h4>
            <p>Visualisez vos données avec des graphiques interactifs et des métriques clés.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📥 Téléchargement Facile</h4>
            <p>Téléchargez vos données au format CSV pour une utilisation ultérieure.</p>
        </div>
        """, unsafe_allow_html=True)

# Page de scraping
def show_scraping():
    st.markdown("<h2>🕷️ Scraping de Données</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <p>Configurez vos paramètres de scraping et lancez la collecte de données depuis Expat-Dakar.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Configuration")
        url = st.selectbox("URL de base", options=["https://dakar-auto.com/senegal/voitures-4", "https://dakar-auto.com/senegal/motos-and-scooters-3", "https://dakar-auto.com/senegal/location-de-voitures-19"], index=0)
        
        max_pages = st.number_input("Nombre de pages à scraper", value=1, min_value=1, step=1)
        
        if st.button("🚀 Lancer le Scraping", key="scrape_btn"):
            print(f"Scraping igor: {url}")
            if url and url == 'https://dakar-auto.com/senegal/voitures-4':
                print(f"Scraping igor v2: {url}")
                scraped_df = scrape_voitures_data(url, max_pages)
                st.session_state.scraped_data = scraped_df
                st.success(f"✅ Scraping terminé ! {len(scraped_df)} données collectées.")
            elif url and url == 'https://dakar-auto.com/senegal/motos-and-scooters-3':
                scraped_df = scrape_motos_data(url, max_pages)
                st.session_state.scraped_data = scraped_df
                st.success(f"✅ Scraping terminé ! {len(scraped_df)} données collectées.")
            elif url and url == 'https://dakar-auto.com/senegal/location-de-voitures-19':
                scraped_df = scrape_location_data(url, max_pages)
                st.session_state.scraped_data = scraped_df
            else:
                print(f"Scraping igor v3: {url}")
                st.error("Veuillez entrer une URL valide.")
    
    with col2:
        st.subheader("Données Scrapées")
        if st.session_state.scraped_data:
            st.dataframe(st.session_state.scraped_data.head())
            
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
        <p>Téléchargez les données déjà scrapées et stockées dans notre base de données.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Liste des fichiers disponibles
    available_files = [
        ('motos_scooters1.csv', 'Motocycles - Lot 1'),
        ('motos_scooters2.csv', 'Motocycles - Lot 2'),
        ('motos_scooters3.csv', 'Motocycles - Lot 3'),
        ('motos_scooters4.csv', 'Motocycles - Lot 4'),
        ('motos_scooters5.csv', 'Motocycles - Lot 5')
    ]
    
    st.subheader("Fichiers Disponibles")
    
    for filename, description in available_files:
        try:
            df = pd.read_csv(f'data/{filename}')
            
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            
            with col1:
                st.write(f"**{description}**")
            
            with col2:
                st.write(f"📊 {df.shape[0]} lignes")
            
            with col3:
                st.write(f"📋 {df.shape[1]} colonnes")
            
            with col4:
                csv_link = download_csv(df, filename.replace('.csv', ''))
                st.markdown(csv_link, unsafe_allow_html=True)
            
            st.divider()
            
        except FileNotFoundError:
            st.warning(f"Fichier {filename} non trouvé.")

# Page dashboard
def show_dashboard():
    st.markdown("<h2>📊 Dashboard Analytique</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <p>Visualisez et analysez vos données avec des graphiques interactifs et des métriques clés.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sélection des données à analyser
    data_source = st.radio(
        "Choisissez la source de données :",
        ["Données scrapées récemment", "Données stockées"]
    )
    
    if data_source == "Données scrapées récemment":
        if st.session_state.scraped_data:
            create_dashboard(st.session_state.scraped_data)
        else:
            st.info("Aucune donnée scrapée récemment. Allez dans l'onglet Scraping pour collecter des données.")
    else:
        # Charger et combiner toutes les données stockées
        all_data = []
        for i in range(1, 6):
            try:
                df = pd.read_csv(f'data/motos_scooters{i}.csv')
                all_data.append(df)
            except FileNotFoundError:
                continue
        
        if all_data:
            combined_df = pd.concat(all_data, ignore_index=True)
            create_dashboard(combined_df)
        else:
            st.warning("Aucune donnée stockée trouvée.")

# Page formulaire d'évaluation
def show_feedback():
    st.markdown("<h2>📝 Évaluation de l'Application</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <p>Aidez-nous à améliorer notre plateforme en partageant votre expérience utilisateur. 
        Utilisez le formulaire ci-dessous pour nous donner votre avis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Intégration du formulaire KoboToolbox
    st.markdown("""
    <div style="display: flex; justify-content: center; margin: 2rem 0;">
        <iframe src="https://ee.kobotoolbox.org/i/kXR3jNKQ" 
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
    <div style="text-align: center; padding: 1rem;">
        <h3>🚗 Navigation</h3>
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




 


