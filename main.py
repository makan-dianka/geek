from test import Person

def eleve(nom, age):
    etat_actuel = Person(nom,age)
    Etat = etat_actuel.getperson()
    return Etat


name = input("nom > ")
age = input( "age > ")

U = eleve(name,age)
print(U)
