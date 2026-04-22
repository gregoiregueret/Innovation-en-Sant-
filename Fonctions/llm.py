from groq import Groq
from config import GROQ_API_KEY, SYSTEM_PROMPT, USER_INSTRUCTIONS, LLM_MODEL, LLM_TEMPERATURE


client = Groq(api_key=GROQ_API_KEY)


def summarize_with_llm(context):
    """
    Génère une synthèse à partir du contexte fourni.
    """

    if not context.strip():
        return "Contexte vide."

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"{USER_INSTRUCTIONS}\n\nContexte :\n{context}"
                }
            ],
            temperature=LLM_TEMPERATURE
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Erreur LLM : {error}"