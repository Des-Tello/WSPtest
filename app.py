from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hola' in incoming_msg:
        msg.body('Hola! ¿Cómo estás?')
    else:
        msg.body('Lo siento, no entiendo tu mensaje.')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)