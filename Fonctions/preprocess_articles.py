"""
===========================================================
Article Preprocessing Module
===========================================================

Description:
------------
Ce module permet de nettoyer et préparer les articles
avant les étapes de filtrage sémantique et d’analyse.

Les traitements réalisés incluent :
- Fusion du titre et du résumé
- Nettoyage du texte brut
- Structuration des données exploitables

Fonctionnalités:
----------------
- Prétraitement des articles
- Nettoyage automatique du texte
- Création d’un champ textuel exploitable
- Préparation des données pour les embeddings

Auteur:
--------
Grégoire Gueret

Projet:
--------
AI Research Assistant

Date:
-----
29 Avril 2026

===========================================================
"""

from Fonctions.clean_text import clean_text


# =========================================================
# Fonction principale
# =========================================================

def preprocess_articles(articles):
    """
    Nettoie et prépare les articles pour les
    étapes suivantes du pipeline.

    Parameters
    ----------
    articles : list
        Liste de dictionnaires contenant au minimum :
        - title
        - summary
        - link
        - category (optionnel)

    Returns
    -------
    list
        Liste d’articles prétraités contenant
        un champ 'text' exploitable pour le
        filtrage sémantique.
    """

    processed = []

    for article in articles:

        title = article.get("title", "")
        summary = article.get("summary", "")
        link = article.get("link", "")
        category = article.get("category", "")

        # Fusion du titre et du résumé
        # afin d’obtenir un texte plus riche
        raw_text = f"{title} {summary}"

        # Nettoyage du texte
        clean = clean_text(raw_text)

        # Construction de l’article prétraité
        processed.append(
            {
                "title": title,
                "summary": summary,
                "text": clean,
                "link": link,
                "category": category,
            }
        )

    return processed