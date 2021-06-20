#module pour convertir les devices " euro, fcfa "
#author : MAKAN DIANKA
#email : makan.dianka@hotmail.com

def calcul_device(device):
    try: 
        if device.lower() == 'e':
            euro = int(input("\n EURO : "))
            franc_fcfa = euro*130
            local = euro*130*5
            print("\n FCFA - XOF \t \t \t \tENTIER - XOF")
            print(' '+str(local)+' Fcfa'+'\t \t \t \t'+str(franc_fcfa))
        elif device.lower() == 'ff':
            fcfa = int(input("\n ENTIER - XOF : "))
            euro = fcfa/130
            euro = int(euro)
            print()
            print(' '+str(euro)+' €')
        elif device.lower() == 'f':
            fcfa = int(input("\n FCFA - XOF : "))
            euro = fcfa/650
            euro = int(euro)
            print()
            print(' '+str(euro)+' €')
        else:
            print("\nSaisissez uniquement (E, F ou FF)")
    except ValueError as error:
        print(f"\n Oups! une erreur s'est produite. Source de l'erreur: {error}\n\n Suggestion : saisissez uniquement les chiffres dans les champs")

n = True
stop = ['ok', 'fin', 'stop', 'n']
while n:
    print("\n\nConvertion de device : 1 Euro = 650 Fcfa")
    print("Selectionnez les options ci-dessous pour Converture.")
    print("quitter [ok, n, fin, stop]")
    device = input("Appuyer (E) pour euro, (F) pour fcfa standart(1=5), (FF) pour fcfa entier(1=1) : ")
    calcul_device(device)
    if device.lower() in stop:
        n=False
        print("\n OK bye.")