import streamlit as st
import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs
import re


def scrape_voitures_data(max_pages):
    """Scraping de voitures avec BeautifulSoup"""
    base_url = 'https://dakar-auto.com/senegal/voitures-4'
    data = []

    for p_index in range(1, max_pages + 1):
        # Construire l'URL
        url = f'{base_url}?page={p_index}' if p_index > 1 else base_url
        print(f"Scraping: {url}, page {p_index}")

        try:
            response = get(url)
            soup = bs(response.text, 'html.parser')

            # Sélectionner les annonces
            containers = soup.select('.listings-cards__list-item')

            for container in containers:
                try:
                    prix_raw = container.select_one('.listing-card__header__price')
                    prix = prix_raw.text.strip() if prix_raw else ''
                    cleaned_price = int(re.sub(r"[^\d]", "", prix)) if prix else None

                    titre = container.select_one('.listing-card__header__title a')
                    nom_complet = titre.text.strip().split() if titre else []
                    marque = nom_complet[0] if nom_complet else None
                    annee = nom_complet[-1] if nom_complet else None

                    localisation_elem = container.select_one('.entry-zone-address')
                    localisation = localisation_elem.text.strip() if localisation_elem else None

                    auteur_elem = container.select_one('.time-author a')
                    publie_par = auteur_elem.text.strip() if auteur_elem else None
                    proprietaire = publie_par[4:] if publie_par else None

                    kilometrage = type_boite = carburant = None
                    attributes = container.select('.listing-card__attribute')

                    for attr in attributes:
                        text = attr.text.strip()
                        icon = attr.select_one('i')
                        if icon and 'icon-road-perspective' in icon['class']:
                            kilometrage = int(text.replace(' km', '').replace(' ',''))
                        elif icon and 'icon-gear-icon' in icon['class']:
                            type_boite = text
                        elif icon and 'icon-fuel' in icon['class']:
                            carburant = text

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
                    print(f"Erreur interne dans un container: {e}")
                    continue

        except Exception as e:
            print(f"Erreur lors du chargement de la page: {e}")
            continue

    # Créer un DataFrame
    df = pd.DataFrame(data)
    print(df)
    return df

def scrape_motos_data(max_pages):
    """Fonction de scraping pour les données de motos"""
    base_url = 'https://dakar-auto.com/senegal/motos-and-scooters-3'
    data = []

    for p_index in range(1, max_pages + 1): 
        # Construire l'URL
        url = f'{base_url}?page={p_index}' if p_index > 1 else base_url
        print(f"Scraping: {url}, page {p_index}")

        try:
            response = get(url)
            soup = bs(response.text, 'html.parser')

            # Sélectionner les annonces
            containers = soup.select('.listings-cards__list-item')

            for container in containers: 
                try:
                    prix_raw = container.select_one('.listing-card__header__price')
                    prix = prix_raw.text.strip() if prix_raw else ''
                    cleaned_price = int(re.sub(r"[^\d]", "", prix)) if prix else None

                    titre = container.select_one('.listing-card__header__title a')
                    nom_complet = titre.text.strip().split() if titre else []
                    marque = nom_complet[0] if nom_complet else None
                    annee = nom_complet[-1] if nom_complet else None
                
                    localisation_elem = container.select_one('.entry-zone-address')
                    localisation = localisation_elem.text.strip() if localisation_elem else None

                    auteur_elem = container.select_one('.time-author a')
                    publie_par = auteur_elem.text.strip() if auteur_elem else None
                    proprietaire = publie_par[4:] if publie_par else None

                    attributes = container.select('.listing-card__attribute')
                    kilometrage = type_boite = carburant = None

                    for attr in attributes:
                        text = attr.text.strip()
                        icon = attr.select_one('i')
                        if icon and 'icon-road-perspective' in icon['class']:
                            kilometrage = int(text.replace(' km', '').replace(' ',''))
                        elif icon and 'icon-gear-icon' in icon['class']:
                            type_boite = text
                        elif icon and 'icon-fuel' in icon['class']:
                            carburant = text

                    voiture = {
                        'V1': marque,
                        'V2': annee,
                        'V3': cleaned_price,
                        'V4': localisation,
                        'V5': kilometrage,
                        'V6': proprietaire
                    }                
                    data.append(voiture)    
                except Exception as e:
                    print(f"Erreur interne dans un container: {e}")
                    continue

        except Exception as e:
            print(f"Erreur lors du chargement de la page: {e}")
            continue

       
    # Créer un DataFrame
    df = pd.DataFrame(data)
    print(df)
    return df

def scrape_location_data(max_pages):
    """Fonction de scraping pour les données de location de voitures"""
    
    base_url = 'https://dakar-auto.com/senegal/location-de-voitures-19'
    data = []

    for p_index in range(1, max_pages + 1): 
        # Construire l'URL
        url = f'{base_url}?page={p_index}' if p_index > 1 else base_url
        print(f"Scraping: {url}, page {p_index}")

        try:
            response = get(url)
            soup = bs(response.text, 'html.parser')

            # Sélectionner les annonces
            containers = soup.select('.listings-cards__list-item')

            for container in containers: 
                try:
                    prix_raw = container.select_one('.listing-card__header__price')
                    prix = prix_raw.text.strip() if prix_raw else ''
                    cleaned_price = int(re.sub(r"[^\d]", "", prix)) if prix else None

                    titre = container.select_one('.listing-card__header__title a')
                    nom_complet = titre.text.strip().split() if titre else []
                    marque = nom_complet[0] if nom_complet else None
                    annee = nom_complet[-1] if nom_complet else None

                    localisation_elem = container.select_one('.entry-zone-address')
                    localisation = localisation_elem.text.strip() if localisation_elem else None

                    auteur_elem = container.select_one('.time-author a')
                    publie_par = auteur_elem.text.strip() if auteur_elem else None
                    proprietaire = publie_par[4:] if publie_par else None
                
                    # Insérer les données scrapées
                    voiture = {
                        'V1': marque,
                        'V2': annee,
                        'V3': cleaned_price,
                        'V4': localisation,
                        'V5': proprietaire,
                    }
                    data.append(voiture)

                except Exception as e:
                    print(f"Erreur interne dans un container: {e}")
                    continue

        except Exception as e:
            print(f"Erreur lors du chargement de la page: {e}")
            continue

    # Créer un DataFrame
    df = pd.DataFrame(data)
    print(df)
    return df