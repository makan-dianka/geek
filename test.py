import os

user = os.getlogin()
path = "c:/users/"+f"{user}"

recherche = ["finance", "portofolio", "dagakane", "pro"]

def verification(path):
    listdir = os.listdir(path)
    dossiers = [d for d in listdir if d.lower() in recherche]
            
    return dossiers
    
print(verification(path))