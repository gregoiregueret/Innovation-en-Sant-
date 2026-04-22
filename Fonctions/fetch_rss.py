# Fonction qui permet de récuperer les flux RSS des sites
import feedparser

def fetch_rss(categories, max_items=10):
    """
    Récupère les derniers articles depuis plusieurs flux RSS arXiv.

    Args:
        categories (list): Liste des catégories (ex: ["cs.AI", "q-bio"])
        max_items (int): Nombre d'articles à récupérer par flux

    Returns:
        list: Liste d'articles (dictionnaires)
    """

    base_url = "https://export.arxiv.org/rss/"
    all_articles = []

    for category in categories:
        url = base_url + category
        feed = feedparser.parse(url)

        for entry in feed.entries[:max_items]:
            all_articles.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "category": category
            })

    return all_articles