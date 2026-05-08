from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Sujet de veille
QUERY = "medical healthcare patient diagnosis hospital clinical biology biomedical"

# Catégories arXiv utilisées pour la veille
RSS_CATEGORIES = [
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
Tu es un analyste expert en veille scientifique.

OBJECTIF :
Extraire les idées clés, les nouveautés et les tendances à partir d’un ou plusieurs articles scientifiques, sans jamais inventer d’information.

PRINCIPE FONDAMENTAL :
Tu dois STRICTEMENT te baser sur le contenu fourni.
→ Interdiction d’ajouter des connaissances externes
→ Interdiction de deviner ou extrapoler sans preuve

Toute affirmation doit être :
- directement présente dans le texte
OU
- déduite explicitement avec justification

Si une information n’est pas clairement présente :
→ indiquer "Non supporté par les données"

"""

USER_INSTRUCTIONS = """
INSTRUCTIONS : 
1. Analyser les articles comme un corpus global
2. Extraire uniquement les informations fiables
3. Identifier les idées communes UNIQUEMENT si elles apparaissent dans plusieurs articles
4. Distinguer clairement :
   - faits (basés sur le texte)
   - interprétations (justifiées)
5. Ne jamais combler les manques

---

FORMAT DE SORTIE (OBLIGATOIRE) :

### 1. TL;DR global (max 5 lignes)
→ uniquement basé sur des éléments explicitement présents

### 2. Idées clés (avec source)
→ chaque idée doit inclure :
- l’idée
- référence implicite (article 1, 2…)
- niveau de confiance : ÉLEVÉ / MOYEN / FAIBLE

Format :
- [Idée] (Source : Article X, Confiance : ÉLEVÉ)

### 3. Nouveautés identifiées
→ uniquement si clairement revendiquées ou démontrées dans les articles
→ sinon écrire : "Non clairement établi"

### 4. Convergences (si plusieurs articles)
→ UNIQUEMENT si plusieurs articles disent explicitement la même chose
→ sinon écrire : "Aucune convergence fiable identifiée"

### 5. Divergences (si présentes)
→ différences explicites entre les articles

### 6. Signaux faibles (optionnel)
→ uniquement si suggérés dans le texte
→ préciser : "Interprétation prudente"

### 7. Ce que l’on peut raisonnablement conclure
→ synthèse prudente, sans extrapolation

### 8. Ce qui reste incertain
→ limites des articles
→ manque d’information

---

CONTRAINTES STRICTES :

- Interdiction d’inventer des tendances
- Interdiction d’utiliser des connaissances externes
- Toujours privilégier la prudence à la complétude
- Si doute → indiquer explicitement l’incertitude
- Réponse concise et structurée

---

ENTRÉE :
"""

TEST_LLM = False

# =========================
# CONFIGURATION EMAIL
# =========================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

GROQ_ROUTER_API_KEY = os.getenv("GROQ_ROUTER_API_KEY")

AVAILABLE_ARXIV_CATEGORIES = [
    "cs.AI",   # Artificial Intelligence
    "cs.AR",   # Hardware Architecture
    "cs.CC",   # Computational Complexity
    "cs.CE",   # Computational Engineering
    "cs.CG",   # Computational Geometry
    "cs.CL",   # Computation and Language (NLP)
    "cs.CR",   # Cryptography and Security
    "cs.CV",   # Computer Vision
    "cs.CY",   # Computers and Society
    "cs.DB",   # Databases
    "cs.DC",   # Distributed Computing (Cloud)
    "cs.DL",   # Digital Libraries
    "cs.DM",   # Discrete Mathematics
    "cs.DS",   # Data Structures and Algorithms
    "cs.ET",   # Emerging Technologies
    "cs.FL",   # Formal Languages
    "cs.GL",   # General Literature
    "cs.GR",   # Graphics
    "cs.GT",   # Game Theory
    "cs.HC",   # Human-Computer Interaction
    "cs.IR",   # Information Retrieval
    "cs.IT",   # Information Theory
    "cs.LG",   # Machine Learning
    "cs.LO",   # Logic in Computer Science
    "cs.MA",   # Multiagent Systems
    "cs.MM",   # Multimedia
    "cs.MS",   # Mathematical Software
    "cs.NA",   # Numerical Analysis
    "cs.NE",   # Neural and Evolutionary Computing
    "cs.NI",   # Networking and Internet Architecture
    "cs.OH",   # Other Computer Science
    "cs.OS",   # Operating Systems
    "cs.PF",   # Performance
    "cs.PL",   # Programming Languages
    "cs.RO",   # Robotics
    "cs.SC",   # Symbolic Computation
    "cs.SD",   # Sound
    "cs.SE",   # Software Engineering
    "cs.SI",   # Social and Information Networks
    "cs.SY"    # Systems and Control
    "q-bio.BM",  # Biomolecules
    "q-bio.CB",  # Cell Behavior
    "q-bio.GN",  # Genomics
    "q-bio.MN",  # Molecular Networks
    "q-bio.NC",  # Neurons and Cognition
    "q-bio.PE",  # Populations and Evolution
    "q-bio.QM",  # Quantitative Methods
    "q-bio.SC",  # Subcellular Processes
    "q-bio.TO"   # Tissues and Organs
]

CATEGORY_ROUTER_SYSTEM_PROMPT = """
Tu es un assistant qui sélectionne des catégories arXiv pertinentes.

Tu dois répondre uniquement avec une liste JSON valide.
Tu ne dois ajouter aucun texte, aucune explication, aucun markdown.

Exemple de réponse valide :
["cs.AI", "cs.LG", "cs.CR"]
"""

CATEGORY_ROUTER_USER_PROMPT = """
Sujet de veille :
{query}

Catégories disponibles :
{categories}

Choisis entre 3 et 6 catégories maximum.

IMPORTANT :
- Choisis UNIQUEMENT les catégories les plus pertinentes
- Ignore les catégories non liées au sujet

Réponds uniquement sous forme de liste JSON :
["cs.AI", "cs.LG"]
"""
