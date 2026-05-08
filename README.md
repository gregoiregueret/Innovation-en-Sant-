# Veille scientifique IA (e-santé / cybersécurité / cloud)

## Objectif
Prototype de veille scientifique basé sur :
- RSS arXiv
- filtrage sémantique (embeddings)
- synthèse LLM
- interface utilisateur Streamlit

## Fonctionnement
1. L’utilisateur saisit un sujet
2. Le système sélectionne automatiquement les catégories arXiv
3. Récupération des articles
4. Filtrage par similarité
5. Synthèse LLM
6. Envoi possible par email

## Installation
pip install -r requirements.txt

## Lancement
streamlit run app.py