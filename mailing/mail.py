import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mailing(sender, pwd, recever):
    """
    mailing prend 3 args pour envoyer un mail.
    sender : mail de l'expéditeur
    pwd    : mdp de l'expéditeur
    recever: mail du destinateur
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, pwd)
    print("login success !")
    
    mail=MIMEMultipart()
    mail['From'] = sender
    mail['To'] = recever
    mail['Subject'] = "Objet de votre e-mail"
    message = "votre message ici"

    mail.attach(MIMEText(message,'plain'))
    text = mail.as_string()
    server.sendmail(sender,recever,text)
    print("le msg a été envoyé à", recever)
    server.quit() 