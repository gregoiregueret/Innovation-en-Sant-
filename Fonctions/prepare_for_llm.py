"""
===========================================================
LLM Context Preparation
===========================================================

Description:
------------
Ce module permet de préparer un contexte textuel structuré
à envoyer à un modèle de langage (LLM).

Les articles filtrés sont :
- triés par pertinence
- limités à un nombre maximal
- formatés dans un contexte clair et lisible

Fonctionnalités:
----------------
- Tri des articles par score
- Sélection des articles les plus pertinents
- Construction d’un contexte optimisé pour le LLM
- Gestion des cas sans résultats

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


# =========================================================
# Fonction principale
# =========================================================

def prepare_for_llm(filtered_articles, max_articles=3):
    """
    Prépare un contexte textuel structuré
    à envoyer au modèle LLM.

    Parameters
    ----------
    filtered_articles : list
        Liste des articles filtrés avec score.

    max_articles : int, optional
        Nombre maximal d’articles à inclure.

    Returns
    -------
    str
        Contexte formaté pour le LLM.
    """

    # Vérification de la présence d’articles
    if not filtered_articles:
        return "Aucun article pertinent trouvé."

    # Tri décroissant selon le score de pertinence
    sorted_articles = sorted(
        filtered_articles,
        key=lambda article: article["score"],
        reverse=True,
    )

    # Sélection des meilleurs articles
    selected_articles = sorted_articles[:max_articles]

    context_parts = []

    # Construction des blocs de contexte
    for i, article in enumerate(selected_articles, start=1):

        block = (
            f"Article {i}\n"
            f"Catégorie : "
            f"{article.get('category', 'inconnue')}\n"
            f"Titre : "
            f"{article.get('title', 'sans titre')}\n"
            f"Résumé : "
            f"{article.get('summary', 'sans résumé')}\n"
            f"Score de pertinence : "
            f"{round(article.get('score', 0), 3)}\n"
        )

        context_parts.append(block)

    # Construction du contexte final
    context = (
        "\n"
        + ("-" * 60)
        + "\n".join(context_parts)
    )

    return context