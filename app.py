import streamlit as st

from Fonctions.fetch_rss import fetch_rss
from Fonctions.preprocess_articles import preprocess_articles
from Fonctions.filter_articles import filter_articles
from Fonctions.prepare_for_llm import prepare_for_llm
from Fonctions.llm import summarize_with_llm
from Fonctions.email_sender import send_email

from config import QUERY, RSS_CATEGORIES, MAX_ARTICLES, THRESHOLD, MAX_LLM_ARTICLES


st.set_page_config(page_title="Veille scientifique e-santé", layout="wide")

st.title("Prototype de veille scientifique en e-santé")

st.markdown("Ce prototype récupère des articles arXiv, filtre les plus pertinents et génère une synthèse avec un LLM.")

# Paramètres utilisateur
st.subheader("Paramètres")

query = st.text_input("Sujet de veille", value=QUERY)
categories_input = st.text_input("Catégories arXiv (séparées par des virgules)", value=", ".join(RSS_CATEGORIES))
max_articles = st.number_input("Nombre d'articles par catégorie", min_value=1, max_value=50, value=MAX_ARTICLES)
threshold = st.slider("Seuil de filtrage", min_value=0.0, max_value=1.0, value=float(THRESHOLD), step=0.05)
max_llm_articles = st.number_input("Nombre d'articles envoyés au LLM", min_value=1, max_value=10, value=MAX_LLM_ARTICLES)
test_llm = st.checkbox("Activer l'appel au LLM", value=False)

if st.button("Lancer la veille"):
    categories = [cat.strip() for cat in categories_input.split(",") if cat.strip()]

    with st.spinner("Récupération des articles..."):
        articles = fetch_rss(categories, max_articles)

    st.success(f"{len(articles)} articles récupérés.")

    if not articles:
        st.warning("Aucun article récupéré.")
        st.stop()

    with st.spinner("Prétraitement des articles..."):
        clean_articles = preprocess_articles(articles)

    with st.spinner("Filtrage sémantique..."):
        filtered_articles = filter_articles(clean_articles, query, threshold=threshold)

    st.info(f"{len(filtered_articles)} articles pertinents retenus.")

    if not filtered_articles:
        st.warning("Aucun article pertinent trouvé avec ce seuil.")
        st.stop()

    st.subheader("Articles retenus")

    for article in filtered_articles:
        with st.expander(f"{article['title']} | score = {round(article['score'], 3)}"):
            st.write(f"**Catégorie :** {article.get('category', 'inconnue')}")
            st.write(f"**Résumé :** {article['summary']}")
            st.write(f"**Lien :** {article['link']}")

    context = prepare_for_llm(filtered_articles, max_articles=max_llm_articles)

    with st.expander("Contexte envoyé au LLM"):
        st.text(context)

    if test_llm:
        with st.spinner("Génération de la synthèse..."):
            summary = summarize_with_llm(context)

        st.subheader("Synthèse LLM")
        st.write(summary)

        recipient_email = st.text_input("Adresse email pour recevoir la synthèse")

        if st.button("Envoyer la synthèse par mail"):
            if not recipient_email.strip():
                st.warning("Merci de renseigner une adresse email.")
            else:
                subject = "Synthèse de veille scientifique en e-santé"
                success, message = send_email(recipient_email, subject, summary)

                if success:
                    st.success(message)
                else:
                    st.error(message)
    else:
        st.warning("Appel LLM désactivé pour économiser les tokens.")