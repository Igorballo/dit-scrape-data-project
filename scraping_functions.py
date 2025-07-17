import streamlit as st
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import re

# Instantier l'objet chrome options
options = webdriver.ChromeOptions() 
# définir l'option d'utiliser chrome en mode headless ( utiliser afin de lancer le script en background)
options.add_argument("--headless=new") 
# initialiser l'instance de chrome driver en mode headless
driver = webdriver.Chrome(options=options)

def scrape_voitures_data(max_pages):
    """Fonction de scraping pour les données de voitures"""
    url = 'https://dakar-auto.com/senegal/voitures-4'
    data = []
    for p_index in range(1,max_pages + 1):
        # url
        if p_index > 1:
            url = f'{url}?page={p_index}'
            
        print(f"Scraping: {url}, page {p_index}")

        # obtenir l'url
        driver.get(url)
        # récupérer les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class = 'listings-cards__list-item mb-md-3 mb-3']")
        # récuperer les informations sur tous les containers
        for container in containers: 
            try:
                prix = container.find_element(By.CSS_SELECTOR, "[class = 'listing-card__header__price font-weight-bold text-uppercase mb-0']").text.strip()
                # Nettoyage du prix : garder uniquement les chiffres
                cleaned_price = re.sub(r"[^\d]", "", prix)
                cleaned_price = int(cleaned_price)

                nom_complet = container.find_element(By.CSS_SELECTOR, ".listing-card__header__title a").text.strip().split()
                marque = nom_complet[0]
                
                annee = nom_complet[-1]
                attributes = container.find_elements(By.CSS_SELECTOR, "[class = 'listing-card__attribute list-inline-item']")
                localisation = container.find_element(By.CSS_SELECTOR, "[class = 'col-12 entry-zone-address']").text.strip()
                publie_par = container.find_element(By.CSS_SELECTOR, "[class = 'time-author m-0'] a").text.strip()
                proprietaire = publie_par[4:]

                # Initialiser les variables
                kilometrage = None
                type_boite = None
                carburant = None

                for attr in attributes:
                    html = attr.get_attribute("innerHTML")
                    if "icon-road-perspective" in html:
                        # Format: 100000 km
                        kilometrage = int(attr.text.strip().replace(' km',''))
                    elif "icon-gear-icon" in html:
                        # Format: Automatique
                        type_boite = attr.text.strip()
                    elif "icon-fuel" in html:
                        # Format: Diesel
                        carburant = attr.text.strip()

                # Insérer les données scrapées
                voiture = {
                    'V1': marque,
                    'V2': annee,
                    'V3': cleaned_price,
                    'V4': localisation,
                    'V5': kilometrage,
                    'V6': type_boite,
                    'V7': carburant,
                    'V8': proprietaire,
                }
                data.append(voiture)    
            except Exception as e:
                print(f"Erreur lors du scraping d'un élément: {e}")
                pass

    df = pd.DataFrame(data)
    print(df)
    return df


def scrape_motos_data(max_pages):
    """Fonction de scraping pour les données de motos"""
    url = 'https://dakar-auto.com/senegal/motos-and-scooters-3'
    data = []

    for p_index in range(1,max_pages + 1):
        # url
        if p_index > 1:
            url = f'{url}?page={p_index}'
            
        print(f"Scraping: {url}")

        # obtenir l'url
        driver.get(url)
        # récupérer les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class = 'listings-cards__list-item mb-md-3 mb-3']")
        # récuperer les informations sur tous les containers
        for container in containers: 
            try:
                prix = container.find_element(By.CSS_SELECTOR, "[class = 'listing-card__header__price font-weight-bold text-uppercase mb-0']").text.strip()
                # Nettoyage du prix : garder uniquement les chiffres
                cleaned_price = re.sub(r"[^\d]", "", prix)
                cleaned_price = int(cleaned_price) 

                nom_complet = container.find_element(By.CSS_SELECTOR, ".listing-card__header__title a").text.strip().split()
                marque = nom_complet[0]
                
                annee = nom_complet[-1]
                
                attributes = container.find_elements(By.CSS_SELECTOR, "[class = 'listing-card__attribute list-inline-item']")
                localisation = container.find_element(By.CSS_SELECTOR, "[class = 'col-12 entry-zone-address']").text.strip()
                publie_par = container.find_element(By.CSS_SELECTOR, "[class = 'time-author m-0'] a").text.strip()
                proprietaire = publie_par[4:]

                for attr in attributes:
                    html = attr.get_attribute("innerHTML")
                    if "icon-road-perspective" in html:
                        # Format: 100000 km
                        kilometrage = int(attr.text.strip().replace(' km',''))
                
                # Insérer les données scrapées
                voiture = {
                    'V1': marque,
                    'V2': annee,
                    'V3': cleaned_price,
                    'V4': localisation,
                    'V5': kilometrage,
                    'V6': proprietaire
                }                
                data.append(voiture)    
            except:
                pass

    df = pd.DataFrame(data)
    print(df)
    return df

def scrape_location_data(max_pages):
    """Fonction de scraping pour les données de location de voitures"""
    
    url = 'https://dakar-auto.com/senegal/location-de-voitures-19'
    data = []
    for p_index in range(1,max_pages + 1):
        # url
        if p_index > 1:
            url = f'{url}?page={p_index}'
            
        print(f"Scraping: {url}, page {p_index}")

        # obtenir l'url
        driver.get(url)
        # récupérer les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class = 'listings-cards__list-item mb-md-3 mb-3']")
        # récuperer les informations sur tous les containers
        for container in containers: 
            try:
                etat = container.find_element(By.CSS_SELECTOR, "[class = 'badge badge-pill badge-primary ml-2']").text
                prix = container.find_element(By.CSS_SELECTOR, "[class = 'listing-card__header__price font-weight-bold text-uppercase mb-0']").text.strip()
                # Nettoyage du prix : garder uniquement les chiffres
                cleaned_price = re.sub(r"[^\d]", "", prix)
                cleaned_price = int(cleaned_price) 

                nom_complet = container.find_element(By.CSS_SELECTOR, ".listing-card__header__title a").text.strip().split()
                marque = nom_complet[0]
                
                annee = nom_complet[-1]
                
                localisation = container.find_element(By.CSS_SELECTOR, "[class = 'col-12 entry-zone-address']").text.strip()
                publie_par = container.find_element(By.CSS_SELECTOR, "[class = 'time-author m-0'] a").text.strip()
                proprietaire = publie_par[4:]
                
                # Insérer les données scrapées
                voiture = {
                    'V1': marque,
                    'V2': annee,
                    'V3': cleaned_price,
                    'V4': localisation,
                    'V5': proprietaire,
                }                
                data.append(voiture)    
            except:
                pass

    df = pd.DataFrame(data)
    print(df)
    return df