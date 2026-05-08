"""
===========================================================
Semantic Article Filtering
===========================================================

Description:
------------
Ce module permet de filtrer automatiquement des articles
en fonction de leur proximité sémantique avec une requête
utilisateur.

Le système utilise :
- Sentence Transformers pour les embeddings
- La similarité cosinus pour mesurer la pertinence

Fonctionnalités:
----------------
- Encodage sémantique des textes
- Calcul de similarité cosinus
- Filtrage automatique par seuil
- Attribution d’un score de pertinence

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

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# Chargement du modèle d'embedding
# =========================================================

model = SentenceTransformer("all-MiniLM-L6-v2")


# =========================================================
# Fonction principale
# =========================================================

def filter_articles(articles, query, threshold=0.15):
    """
    Filtre les articles selon leur proximité
    sémantique avec une requête utilisateur.

    Parameters
    ----------
    articles : list
        Liste d’articles prétraités.

    query : str
        Sujet de veille ou requête sémantique.

    threshold : float, optional
        Seuil minimal de pertinence.

    Returns
    -------
    list
        Liste des articles retenus avec
        leur score de pertinence.
    """

    # Vérification de la présence d’articles
    if not articles:
        return []

    # Extraction des textes
    texts = [article["text"] for article in articles]

    # Génération des embeddings
    doc_embeddings = model.encode(texts)
    query_embedding = model.encode([query])

    # Calcul des similarités cosinus
    scores = cosine_similarity(
        query_embedding,
        doc_embeddings
    )[0]

    filtered = []

    # Filtrage des articles pertinents
    for article, score in zip(articles, scores):

        if score >= threshold:

            filtered.append(
                {
                    "title": article.get("title", ""),
                    "summary": article.get("summary", ""),
                    "text": article.get("text", ""),
                    "link": article.get("link", ""),
                    "category": article.get("category", ""),
                    "score": float(score),
                }
            )

    return filtered