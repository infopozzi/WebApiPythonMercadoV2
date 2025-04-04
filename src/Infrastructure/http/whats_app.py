from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


def Enviar_mensagem(telefoneDestino, texto):
    account_sid = "AC7567d079d02433ec7b26f6e7d6d7fb61"
    auth_token = "c1fd9cda01cff4086efdc3fd5e09d14e"
    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+55' + telefoneDestino

    client.messages.create(body=texto,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def Responder_mensagem():
    pass
