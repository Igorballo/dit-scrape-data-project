# 🚗 Plateforme de Scraping - AutoScrape Dakar

Une application Streamlit moderne pour la collecte, l'analyse et le téléchargement de données automobiles depuis AutoScraper.

## 🎯 Fonctionnalités

### 📋 Page d'Accueil
- Présentation claire de la plateforme
- Description des fonctionnalités principales
- Interface moderne et intuitive

### 🕷️ Scraping de Données
- Configuration flexible des paramètres de scraping
- Support multi-pages

### 📥 Téléchargement
- Accès aux données déjà scrapées
- Téléchargement au format CSV
- Informations détaillées sur chaque fichier

### 📊 Dashboard Analytique
- Visualisations interactives avec Plotly
- Métriques clés (prix moyen, année moyenne, etc.)
- Graphiques de distribution et de répartition

### 📝 Formulaire d'Évaluation
- Évaluation globale de l'application
- Commentaires et suggestions
- Sauvegarde des retours utilisateur

## 🚀 Installation et Utilisation

### Prérequis
- Python 3.7+
- pip

### Installation

1. **Cloner ou télécharger le projet**
```bash
git clone git@github.com:Igorballo/dit-scrape-data-project.git
cd dit-scrape-data-project
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Lancer l'application**
```bash
streamlit run my_data_app.py
```

4. **Accéder à l'application**
Ouvrez votre navigateur et allez sur `http://localhost:8501`

## 🛠️ Architecture du Code

### Structure Modulaire
Le code est organisé en fonctions modulaires pour faciliter la maintenance :

- **`main()`** : Point d'entrée principal avec navigation
- **`show_home()`** : Page d'accueil
- **`show_scraping()`** : Interface de scraping
- **`show_download()`** : Gestion des téléchargements
- **`show_dashboard()`** : Dashboard analytique
- **`show_feedback()`** : Formulaire d'évaluation

### Fonctions Utilitaires
- **`scrape_motos_data()`** : Logique de scraping
- **`clean_data()`** : Nettoyage des données
- **`create_dashboard()`** : Création des visualisations
- **`download_csv()`** : Génération des liens de téléchargement


## 📊 Déploiement sur Streamlit Cloud

1. **Préparer le projet**
   - Assurez-vous que tous les fichiers sont dans le repository
   - Vérifiez que `requirements.txt` est à jour

2. **Déployer sur Streamlit Cloud**
   - Connectez votre repository GitHub à Streamlit Cloud
   - Configurez le chemin vers `my_data_app.py`
   - Déployez l'application


## 🤝 Contribution

Pour contribuer au projet :

1. Fork le repository
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Créez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de développement

---

**Développé avec ❤️ pour la communauté de scraping de données**