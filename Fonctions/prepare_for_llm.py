def prepare_for_llm(filtered_articles, max_articles=3):
    """
    Prépare un contexte textuel propre à envoyer au LLM.

    Args:
        filtered_articles (list): Articles filtrés avec score.
        max_articles (int): Nombre maximum d'articles à inclure.

    Returns:
        str: Contexte formaté pour le LLM.
    """

    if not filtered_articles:
        return "Aucun article pertinent trouvé."

    # Tri décroissant selon le score
    sorted_articles = sorted(
        filtered_articles,
        key=lambda article: article["score"],
        reverse=True
    )

    # On garde seulement les meilleurs
    selected_articles = sorted_articles[:max_articles]

    context_parts = []

    for i, article in enumerate(selected_articles, start=1):
        block = (
            f"Article {i}\n"
            f"Catégorie : {article.get('category', 'inconnue')}\n"
            f"Titre : {article.get('title', 'sans titre')}\n"
            f"Résumé : {article.get('summary', 'sans résumé')}\n"
            f"Score de pertinence : {round(article.get('score', 0), 3)}\n"
        )
        context_parts.append(block)

    context = "\n" + ("-" * 60) + "\n".join(context_parts)

    return context