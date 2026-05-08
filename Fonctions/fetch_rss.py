"""
===========================================================
ArXiv RSS Fetcher
===========================================================

Description:
------------
Ce module permet de récupérer automatiquement les
articles récents depuis les flux RSS d’arXiv.

Fonctionnalités:
----------------
- Récupération de plusieurs flux RSS
- Extraction des informations principales
- Gestion des catégories arXiv
- Création d’une liste structurée d’articles

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

import feedparser


# =========================================================
# Fonction principale
# =========================================================

def fetch_rss(categories, max_items=10):
    """
    Récupère les derniers articles depuis plusieurs
    flux RSS arXiv.

    Parameters
    ----------
    categories : list
        Liste des catégories arXiv
        (exemple : ["cs.AI", "q-bio"]).

    max_items : int, optional
        Nombre maximum d’articles récupérés
        par flux RSS.

    Returns
    -------
    list
        Liste de dictionnaires contenant
        les informations des articles.
    """

    base_url = "https://export.arxiv.org/rss/"
    all_articles = []

    for category in categories:

        url = base_url + category

        # Lecture du flux RSS
        feed = feedparser.parse(url)

        # Extraction des articles
        for entry in feed.entries[:max_items]:

            all_articles.append(
                {
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "link": entry.get("link", ""),
                    "category": category,
                }
            )

    return all_articles