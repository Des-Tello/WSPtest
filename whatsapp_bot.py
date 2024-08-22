from twilio.rest import Client

# Tus credenciales de Twilio
account_sid = 'AC4ff994eca2d79c4abfa1066e686a5b49'
auth_token = 'f1829258232a087b254167ba5ed5b615'
client = Client(account_sid, auth_token)

# Número de WhatsApp de Twilio y el número de destino
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+56962341118'

# Enviar un mensaje
message = client.messages.create(
    body='WUAJAJAJ',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(message.sid)