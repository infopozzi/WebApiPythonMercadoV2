from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


def Enviar_mensagem(telefoneDestino, texto):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    from_whatsapp_number = ''
    to_whatsapp_number = 'whatsapp:+55' + telefoneDestino

    client.messages.create(body=texto,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def Responder_mensagem():
    pass
