from config import EMAIL_SENDER, EMAIL_PASSWORD
from Fonctions.send_email import send_email

print("EMAIL_SENDER =", EMAIL_SENDER)
print("EMAIL_PASSWORD présent ? ->", EMAIL_PASSWORD is not None)
print("Longueur EMAIL_PASSWORD =", len(EMAIL_PASSWORD) if EMAIL_PASSWORD else 0)
print("EMAIL_SENDER =", EMAIL_PASSWORD)

for i in range (5):
    send_email("palomasaintremy@gmail.com",  f"Bonjour PALOMA {i}", "Comment vas tu ajd ?")