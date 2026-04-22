from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def filter_articles(articles, query, threshold=0.15):
    """
    Filtre les articles selon leur proximité sémantique avec la requête.

    Args:
        articles (list): Liste d'articles prétraités.
        query (str): Sujet de veille / requête sémantique.
        threshold (float): Seuil minimal de pertinence.

    Returns:
        list: Articles retenus avec leur score.
    """

    if not articles:
        return []

    texts = [article["text"] for article in articles]

    doc_embeddings = model.encode(texts)
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, doc_embeddings)[0]

    filtered = []

    for article, score in zip(articles, scores):
        if score >= threshold:
            filtered.append({
                "title": article.get("title", ""),
                "summary": article.get("summary", ""),
                "text": article.get("text", ""),
                "link": article.get("link", ""),
                "category": article.get("category", ""),
                "score": float(score)
            })

    return filtered