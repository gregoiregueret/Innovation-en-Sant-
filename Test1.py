from Fonctions.fetch_rss import fetch_rss
from Fonctions.preprocess_articles import preprocess_articles
from Fonctions.filter_articles import filter_articles
from Fonctions.prepare_for_llm import prepare_for_llm
from Fonctions.llm import summarize_with_llm

from config import QUERY, RSS_CATEGORIES, MAX_ARTICLES, THRESHOLD, MAX_LLM_ARTICLES,TEST_LLM

def main():
    # 1. Récupération des articles depuis les catégories RSS
    articles = fetch_rss(RSS_CATEGORIES, MAX_ARTICLES)
    print("Nombre d'articles récupérés :", len(articles))

    if len(articles) > 0:
        print("Premier titre brut :", articles[0]["title"])
        print("Catégorie :", articles[0]["category"])
        print("-----")
    else:
        print("Aucun article récupéré.")
        return

    # 2. Prétraitement / nettoyage
    clean_articles = preprocess_articles(articles)
    print("Nombre d'articles après preprocess :", len(clean_articles))

    if len(clean_articles) > 0:
        print("Premier texte nettoyé :", clean_articles[0]["text"][:300])
        print("-----")
    else:
        print("Aucun article après preprocess.")
        return

    # 3. Filtrage sémantique
    filtered_articles = filter_articles(clean_articles, QUERY, threshold=THRESHOLD)

    print("Nombre d'articles filtrés :", len(filtered_articles))
    print("-----")

    if not filtered_articles:
        print("Aucun article pertinent trouvé avec ce seuil.")
        return

    # 4. Affichage des articles retenus
    for article in filtered_articles:
        print("SCORE :", round(article["score"], 3))
        print("TEXT :", article["text"][:250])
        print("LINK :", article["link"])
        print("------")

    # 5. Préparation du contexte pour le LLM
    context = prepare_for_llm(filtered_articles, max_articles=MAX_LLM_ARTICLES)

    print("===== CONTEXTE ENVOYÉ AU LLM =====")
    print(context[:4000])  # on limite l'affichage pour rester lisible

    if TEST_LLM:
        summary = summarize_with_llm(context)
        print("\n===== SYNTHÈSE DU LLM =====")
        print(summary)
    else:
        print("\nAppel LLM désactivé pour économiser les tokens.")


if __name__ == "__main__":
    main()

# MEttre sous une forme qui va bien, l'envoyer par mail, un resultat user frendly
