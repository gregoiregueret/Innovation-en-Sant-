"""
===========================================================
Scientific Watch Streamlit Application
===========================================================

Description:
------------
Cette application Streamlit permet de réaliser une veille
scientifique automatisée à partir des flux RSS arXiv.

Le prototype récupère les articles scientifiques, les
prétraite, filtre les plus pertinents selon une requête
utilisateur, puis génère éventuellement une synthèse avec
un modèle de langage.

Fonctionnalités:
----------------
- Interface web avec Streamlit
- Récupération automatique d’articles arXiv
- Suggestion automatique des catégories arXiv
- Filtrage sémantique des articles
- Préparation du contexte pour le LLM
- Génération optionnelle d’une synthèse
- Envoi possible de la synthèse par email
- Gestion de la mémoire de session Streamlit

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

import streamlit as st

from Fonctions.category_router import suggest_arxiv_categories
from Fonctions.fetch_rss import fetch_rss
from Fonctions.filter_articles import filter_articles
from Fonctions.llm import summarize_with_llm
from Fonctions.prepare_for_llm import prepare_for_llm
from Fonctions.preprocess_articles import preprocess_articles
from Fonctions.send_email import send_email

from config import (
    AVAILABLE_ARXIV_CATEGORIES,
    MAX_ARTICLES,
    MAX_LLM_ARTICLES,
    QUERY,
    RSS_CATEGORIES,
    THRESHOLD,
)


# =========================================================
# Configuration de la page Streamlit
# =========================================================

st.set_page_config(
    page_title="Veille scientifique",
    layout="wide",
)


# =========================================================
# Titre et description de l'application
# =========================================================

st.title("Prototype de veille scientifique")

st.markdown(
    "Ce prototype récupère des articles arXiv, filtre les plus "
    "pertinents et génère une synthèse avec un LLM."
)


# =========================================================
# Initialisation de la mémoire de session
# =========================================================

if "veille_lancee" not in st.session_state:
    st.session_state.veille_lancee = False

if "filtered_articles" not in st.session_state:
    st.session_state.filtered_articles = []

if "context" not in st.session_state:
    st.session_state.context = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "suggested_categories" not in st.session_state:
    st.session_state.suggested_categories = RSS_CATEGORIES


# =========================================================
# Paramètres utilisateur
# =========================================================

st.subheader("Paramètres")

query = st.text_input(
    "Sujet de veille",
    value=QUERY,
)

if st.button("Suggérer automatiquement les catégories arXiv"):

    with st.spinner("Sélection automatique des catégories..."):
        st.session_state.suggested_categories = suggest_arxiv_categories(
            query
        )

categories = st.multiselect(
    "Catégories arXiv utilisées",
    options=AVAILABLE_ARXIV_CATEGORIES,
    default=st.session_state.suggested_categories,
)

max_articles = st.number_input(
    "Nombre d'articles par catégorie",
    min_value=1,
    max_value=50,
    value=MAX_ARTICLES,
)

threshold = st.slider(
    "Seuil de filtrage",
    min_value=0.0,
    max_value=1.0,
    value=float(THRESHOLD),
    step=0.05,
)

max_llm_articles = st.number_input(
    "Nombre d'articles envoyés au LLM",
    min_value=1,
    max_value=10,
    value=MAX_LLM_ARTICLES,
)

test_llm = st.checkbox(
    "Activer l'appel au LLM",
    value=False,
)


# =========================================================
# Lancement de la veille scientifique
# =========================================================

if st.button("Lancer la veille"):

    if not categories:
        st.warning("Merci de sélectionner au moins une catégorie arXiv.")
        st.stop()

    with st.spinner("Récupération des articles..."):
        articles = fetch_rss(
            categories,
            max_articles,
        )

    if not articles:
        st.warning("Aucun article récupéré.")
        st.session_state.veille_lancee = False

    else:
        clean_articles = preprocess_articles(articles)

        filtered_articles = filter_articles(
            clean_articles,
            query,
            threshold=threshold,
        )

        if not filtered_articles:
            st.warning("Aucun article pertinent trouvé avec ce seuil.")
            st.session_state.veille_lancee = False

        else:
            context = prepare_for_llm(
                filtered_articles,
                max_articles=max_llm_articles,
            )

            summary = ""

            if test_llm:

                with st.spinner("Génération de la synthèse..."):
                    summary = summarize_with_llm(context)

            # Sauvegarde des résultats dans la session
            st.session_state.veille_lancee = True
            st.session_state.filtered_articles = filtered_articles
            st.session_state.context = context
            st.session_state.summary = summary


# =========================================================
# Affichage des résultats
# =========================================================

if st.session_state.veille_lancee:

    filtered_articles = st.session_state.filtered_articles
    context = st.session_state.context
    summary = st.session_state.summary

    st.success(f"{len(filtered_articles)} articles pertinents retenus.")

    st.subheader("Articles retenus")

    for article in filtered_articles:

        title = article["title"]
        score = round(article["score"], 3)

        with st.expander(f"{title} | score = {score}"):

            st.write(
                f"**Catégorie :** "
                f"{article.get('category', 'inconnue')}"
            )

            st.write(f"**Résumé :** {article['summary']}")
            st.write(f"**Lien :** {article['link']}")

    with st.expander("Contexte envoyé au LLM"):
        st.text(context)

    if test_llm:

        st.subheader("Synthèse LLM")
        st.write(summary)

        recipient_email = st.text_input(
            "Adresse email pour recevoir la synthèse",
            key="recipient_email",
        )

        if st.button("Envoyer la synthèse par mail"):

            if not recipient_email.strip():
                st.warning("Merci de renseigner une adresse email.")

            else:
                subject = "Synthèse de veille scientifique en e-santé"

                success, message = send_email(
                    recipient_email,
                    subject,
                    summary,
                )

                if success:
                    st.success(message)

                else:
                    st.error(message)

    else:
        st.warning("Appel LLM désactivé pour économiser les tokens.")