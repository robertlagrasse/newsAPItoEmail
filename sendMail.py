import smtplib
import ssl
import json

def send(receiver, message):
    with open('data/creds.json', 'r') as file:
        creds = json.loads(file.read())
        username = creds['username']
        password = creds['password']
        host = creds['host']
        port = creds['port']

        context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)