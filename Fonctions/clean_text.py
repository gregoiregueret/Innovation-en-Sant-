"""
===========================================================
Text Cleaning Utilities
===========================================================

Description:
------------
Ce module contient des fonctions utilitaires permettant
de nettoyer du texte brut avant traitement.

Fonctionnalités:
----------------
- Suppression des balises HTML
- Réduction des espaces multiples
- Nettoyage des espaces inutiles

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

import re


# =========================================================
# Fonction principale
# =========================================================

def clean_text(text):
    """
    Nettoie un texte brut.

    Actions réalisées :
    -------------------
    - Supprime les balises HTML
    - Réduit les espaces multiples
    - Supprime les espaces inutiles
      en début et fin de chaîne

    Parameters
    ----------
    text : str
        Texte brut à nettoyer.

    Returns
    -------
    str
        Texte nettoyé.
    """

    # Suppression des balises HTML
    text = re.sub(r"<.*?>", "", text)

    # Remplacement des espaces multiples
    text = re.sub(r"\s+", " ", text)

    # Nettoyage final
    return text.strip()