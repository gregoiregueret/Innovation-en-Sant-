"""
===========================================================
LLM Summarization Module
===========================================================

Description:
------------
Ce module permet de générer automatiquement une synthèse
à partir d’un contexte textuel en utilisant un modèle
de langage (LLM) via l’API Groq.

Fonctionnalités:
----------------
- Génération de synthèses automatiques
- Intégration avec l’API Groq
- Gestion des prompts système et utilisateur
- Gestion des erreurs de génération

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

from groq import Groq

from config import (
    GROQ_API_KEY,
    LLM_MODEL,
    LLM_TEMPERATURE,
    SYSTEM_PROMPT,
    USER_INSTRUCTIONS,
)


# =========================================================
# Initialisation du client Groq
# =========================================================

client = Groq(api_key=GROQ_API_KEY)


# =========================================================
# Fonction principale
# =========================================================

def summarize_with_llm(context):
    """
    Génère une synthèse à partir du contexte fourni.

    Parameters
    ----------
    context : str
        Texte ou contexte à résumer.

    Returns
    -------
    str
        Synthèse générée par le modèle LLM
        ou message d’erreur.
    """

    # Vérification du contexte
    if not context.strip():
        return "Contexte vide."

    try:

        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": (
                        f"{USER_INSTRUCTIONS}\n\n"
                        f"Contexte :\n{context}"
                    ),
                },
            ],
            temperature=LLM_TEMPERATURE,
        )

        return response.choices[0].message.content

    except Exception as error:

        return f"Erreur LLM : {error}"