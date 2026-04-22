from cle_groq import GROQ_API_KEY

# Sujet de veille
QUERY = "medical healthcare patient diagnosis hospital clinical biology biomedical"

# Catégories arXiv utilisées pour la veille
RSS_CATEGORIES = [
    "cs.AI",
    "cs.LG",
    "q-bio"
]

# Nombre d'articles récupérés par catégorie
MAX_ARTICLES = 10

# Seuil de filtrage sémantique
THRESHOLD = 0.15

# Nombre maximum d'articles envoyés au LLM
MAX_LLM_ARTICLES = 3

# Clé API Groq
GROQ_API_KEY = GROQ_API_KEY

LLM_MODEL = "llama-3.1-8b-instant"
LLM_TEMPERATURE = 0.2

SYSTEM_PROMPT = """
Tu es un assistant spécialisé en veille scientifique en e-santé.

Tu dois :
- produire une synthèse claire et concise
- rester fidèle aux informations fournies
- ne jamais inventer d'information
- rédiger en français
"""

USER_INSTRUCTIONS = """
Voici plusieurs résumés d'articles scientifiques.

Tâche :
- fais une synthèse en 5 points maximum
- identifie les thèmes principaux
- mets en évidence les applications en santé
- souligne les tendances si elles existent
"""

TEST_LLM = False

# =========================
# CONFIGURATION EMAIL
# =========================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_SENDER = "tonadresse@gmail.com"
EMAIL_PASSWORD = "ton_mot_de_passe_application"