
from twilio.rest import Client


class MessageSender:

    account_sid = 'AC30fa14419c690035d5b08c77bed00c1b'
    auth_token = 'd8698fc4463349f10aba0564487b01e2'
    client = Client(account_sid, auth_token)
    @classmethod

    def send(clc,message):
        messagevi = clc.client.messages.create(body=message,from_='+18509403541',to='+919605471074')
        messagejio = clc.client.messages.create(body=message,from_='+18509403541',to='+916282299760')



