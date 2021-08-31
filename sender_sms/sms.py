import os
from twilio.rest import Client

def sms(exp, dest, msg):
    """
    sms prend 3 str args
    exp : numéro de l'expéditeur (twilio)
    dest : numéro du destinateur, (twilio) si le compte vérifie tjr le num.
    msg  : contenu du message
    """
    account_sid = os.environ['account_sid_twilio']
    auth_token = os.environ['auth_token_twilio']
    number_twilio = os.environ["number_twilio"]
    
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
             body= msg,
             from_= exp,
             to= dest
         )
    
    #print(message.sid)
