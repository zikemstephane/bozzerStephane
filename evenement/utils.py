import os
from twilio.rest import Client
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

def envoyer_sms(numero, message):
    # Récupérer les variables d'environnement
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not account_sid or not auth_token or not twilio_number:
        raise ValueError("Les informations Twilio ne sont pas correctement définies dans .env")

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=twilio_number,
        to=numero
    )
