# 🚗 Plateforme de Scraping - Expat Dakar

Une application Streamlit moderne pour la collecte, l'analyse et le téléchargement de données automobiles depuis Expat-Dakar.

## 🎯 Fonctionnalités

### 📋 Page d'Accueil
- Présentation claire de la plateforme
- Description des fonctionnalités principales
- Interface moderne et intuitive

### 🕷️ Scraping de Données
- Configuration flexible des paramètres de scraping
- Support multi-pages
- Barre de progression en temps réel
- Gestion d'erreurs robuste

### 📥 Téléchargement
- Accès aux données déjà scrapées
- Téléchargement au format CSV
- Informations détaillées sur chaque fichier

### 📊 Dashboard Analytique
- Visualisations interactives avec Plotly
- Métriques clés (prix moyen, année moyenne, etc.)
- Graphiques de distribution et de répartition
- Support des données scrapées récemment et stockées

### 📝 Formulaire d'Évaluation
- Évaluation globale de l'application
- Notation par fonctionnalité
- Commentaires et suggestions
- Sauvegarde des retours utilisateur

## 🚀 Installation et Utilisation

### Prérequis
- Python 3.7+
- pip

### Installation

1. **Cloner ou télécharger le projet**
```bash
git clone <votre-repo>
cd examen-data-collection
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

## 📁 Structure du Projet

```
examen-data-collection/
├── my_data_app.py          # Application principale
├── requirements.txt         # Dépendances Python
├── README.md              # Documentation
└── data/                  # Données scrapées
    ├── motos_scooters1.csv
    ├── motos_scooters2.csv
    ├── motos_scooters3.csv
    ├── motos_scooters4.csv
    └── motos_scooters5.csv
```

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

## 🎨 Interface Utilisateur

### Design Moderne
- Interface responsive avec CSS personnalisé
- Navigation par sidebar intuitive
- Cartes d'information stylisées
- Boutons avec effets de survol

### Expérience Utilisateur
- Navigation fluide entre les pages
- Feedback visuel pour toutes les actions
- Barres de progression pour les opérations longues
- Messages d'erreur et de succès clairs

## 🔧 Personnalisation

### Modifier le Scraping
Pour adapter le scraping à vos besoins, modifiez la fonction `scrape_motos_data()` :

```python
def scrape_motos_data(url, max_pages=5):
    # Remplacez la simulation par votre logique de scraping réelle
    # Utilisez requests et BeautifulSoup pour scraper le site
    pass
```

### Ajouter de Nouvelles Visualisations
Dans la fonction `create_dashboard()`, ajoutez vos graphiques :

```python
# Exemple d'ajout d'un nouveau graphique
fig_new = px.scatter(df_clean, x='Prix_Numerique', y='Kilometrage_Numerique')
st.plotly_chart(fig_new, use_container_width=True)
```

### Personnaliser le Style
Modifiez la section CSS dans le code pour changer l'apparence :

```python
st.markdown("""
<style>
    .main-header {
        /* Vos styles personnalisés */
    }
</style>
""", unsafe_allow_html=True)
```

## 📊 Déploiement sur Streamlit Cloud

1. **Préparer le projet**
   - Assurez-vous que tous les fichiers sont dans le repository
   - Vérifiez que `requirements.txt` est à jour

2. **Déployer sur Streamlit Cloud**
   - Connectez votre repository GitHub à Streamlit Cloud
   - Configurez le chemin vers `my_data_app.py`
   - Déployez l'application

3. **Configuration avancée**
   - Ajoutez des variables d'environnement si nécessaire
   - Configurez les permissions d'accès aux données

## 🐛 Dépannage

### Problèmes Courants

**Erreur de dépendances :**
```bash
pip install --upgrade -r requirements.txt
```

**Problème de port :**
```bash
streamlit run my_data_app.py --server.port 8502
```

**Fichiers de données manquants :**
- Vérifiez que le dossier `data/` existe
- Assurez-vous que les fichiers CSV sont présents

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