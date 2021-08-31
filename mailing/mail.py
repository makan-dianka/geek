import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailing(sender, pwd, recever, objet, msg):
    """
    mailing prend 5 args str pour envoyer un mail.
    sender : mail de l'expéditeur
    pwd    : mdp de l'expéditeur
    recever: mail du destinateur
    objet  : objet de msg
    msg    : contenu du msg
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, pwd)
    print("login success !")
    
    mail=MIMEMultipart()
    mail['From'] = sender
    mail['To'] = recever
    mail['Subject'] = objet
    message = msg

    mail.attach(MIMEText(message,'plain'))
    text = mail.as_string()
    server.sendmail(sender,recever,text)
    print("le msg a été envoyé à", recever)
    server.quit() 