"""
===========================================================
ArXiv Category Router
===========================================================

Description:
------------
Ce module utilise un modèle Groq (LLM) afin de suggérer
automatiquement des catégories arXiv pertinentes à partir
d’une requête utilisateur.

Fonctionnalités:
----------------
- Génération dynamique de catégories arXiv
- Validation des catégories retournées
- Gestion des erreurs avec catégories par défaut
- Intégration avec l’API Groq

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

import json

from groq import Groq

from config import (
    AVAILABLE_ARXIV_CATEGORIES,
    CATEGORY_ROUTER_SYSTEM_PROMPT,
    CATEGORY_ROUTER_USER_PROMPT,
    GROQ_ROUTER_API_KEY,
)

# =========================================================
# Initialisation du client Groq
# =========================================================

router_client = Groq(api_key=GROQ_ROUTER_API_KEY)


# =========================================================
# Fonction principale
# =========================================================

def suggest_arxiv_categories(query):
    """
    Suggère des catégories arXiv pertinentes à partir
    d'une requête utilisateur.

    Parameters
    ----------
    query : str
        Requête utilisateur.

    Returns
    -------
    list
        Liste des catégories arXiv valides.
    """

    categories_text = ", ".join(AVAILABLE_ARXIV_CATEGORIES)

    prompt = CATEGORY_ROUTER_USER_PROMPT.format(
        query=query,
        categories=categories_text,
    )

    try:
        response = router_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": CATEGORY_ROUTER_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content.strip()

        print("Réponse brute du LLM :", content)

        suggested = json.loads(content)

        valid_categories = [
            category
            for category in suggested
            if category in AVAILABLE_ARXIV_CATEGORIES
        ]

        # Catégories par défaut si aucune catégorie valide
        # n'est détectée
        if not valid_categories:
            return ["cs.AI", "cs.LG"]

        return valid_categories

    except Exception as error:
        print("ERREUR CATEGORY ROUTER :", error)

        return ["cs.AI", "cs.LG"]


# =========================================================
# Exemple d'utilisation
# =========================================================

if __name__ == "__main__":

    result = suggest_arxiv_categories(
        "AI in cybersecurity and the cloud, for businesses"
    )

    print(result)