from twilio.rest import Client
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de Twilio desde las variables de entorno
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Obtener los números de WhatsApp desde las variables de entorno
from_whatsapp_number = os.getenv('FROM_WHATSAPP_NUMBER')
to_whatsapp_number = os.getenv('TO_WHATSAPP_NUMBER')

# Enviar un mensaje
message = client.messages.create(
    body='WUAJAJAJ',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(message.sid)
