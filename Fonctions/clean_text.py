import re


def clean_text(text):
    """
    Nettoie un texte brut :
    - supprime les balises HTML
    - réduit les espaces multiples
    - enlève les espaces en début et fin
    """

    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()