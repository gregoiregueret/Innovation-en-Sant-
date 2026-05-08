"""
===========================================================
Email Sending Module
===========================================================

Description:
------------
Ce module permet l’envoi d’emails en texte brut
via un serveur SMTP.

Fonctionnalités:
----------------
- Connexion sécurisée SMTP
- Authentification automatique
- Envoi d’emails texte
- Gestion des erreurs d’envoi

Auteur:
--------
Grégoire Gueret

Projet:
--------
AI Research Assistant

Date:
-----
29 Avril 2026

===========================================================
"""

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import (
    EMAIL_PASSWORD,
    EMAIL_SENDER,
    SMTP_PORT,
    SMTP_SERVER,
)


# =========================================================
# Fonction principale
# =========================================================

def send_email(recipient_email, subject, body):
    """
    Envoie un email en texte brut via SMTP.

    Parameters
    ----------
    recipient_email : str
        Adresse email du destinataire.

    subject : str
        Sujet de l’email.

    body : str
        Contenu du message.

    Returns
    -------
    tuple
        Tuple contenant :
        - bool : statut de succès
        - str : message d’information
    """

    try:

        # Création du message
        msg = MIMEMultipart()

        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Ajout du contenu texte
        msg.attach(
            MIMEText(body, "plain", "utf-8")
        )

        # Connexion au serveur SMTP
        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
        )

        # Sécurisation de la connexion
        server.starttls()

        # Authentification
        server.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD,
        )

        # Envoi du message
        server.sendmail(
            EMAIL_SENDER,
            recipient_email,
            msg.as_string(),
        )

        # Fermeture de la connexion
        server.quit()

        return True, "Email envoyé avec succès."

    except Exception as error:

        return (
            False,
            f"Erreur lors de l'envoi du mail : {error}",
        )