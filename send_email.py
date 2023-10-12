import smtplib, ssl
import os


def contactMe(message):
    host = "smtp.gmail.com"
    port = 465
    username = "josea789@gmail.com"
    password = "ntls ufmf icxl czho"
    receiver = "josea789@gmail.com"
    context = ssl.create_default_context()
    message_encoded = message.encode("utf-8")
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_encoded)

