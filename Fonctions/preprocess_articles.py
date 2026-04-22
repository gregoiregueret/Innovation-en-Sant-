from Fonctions.clean_text import clean_text


def preprocess_articles(articles):
    """
    Nettoie et prépare les articles pour les étapes suivantes.

    Args:
        articles (list): Liste de dictionnaires contenant au minimum
                         'title', 'summary', 'link' et éventuellement 'category'.

    Returns:
        list: Liste d'articles prétraités avec un champ 'text' exploitable
              pour le filtrage sémantique.
    """

    processed = []

    for article in articles:
        title = article.get("title", "")
        summary = article.get("summary", "")
        link = article.get("link", "")
        category = article.get("category", "")

        # On fusionne titre + résumé pour avoir un texte plus informatif
        raw_text = f"{title} {summary}"
        clean = clean_text(raw_text)

        processed.append({
            "title": title,
            "summary": summary,
            "text": clean,
            "link": link,
            "category": category
        })

    return processed