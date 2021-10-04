produits = {
    'samsung J5': 150, 'samsung J7': 220,
    'samsung A10': 120,  'samsung A50': 350,
    'samsung S8': 280
    }

l = {}

def calcul(produits):
    total = 0
    for i in produits:
        total += i
        
    return total

def per(p):
    per20 = p // 100 * 20
    
    return per20

def client(nom, select1, select2):
    liste = {}
    if select1 in produits.keys():
        liste[select1] = produits[select1]
    if select2 in produits.keys():
        liste[select2] = produits[select2]
        
    total_prod = [i for i in liste.values()]
    c = calcul(total_prod)
    p = c - per(c)
    
    print()
    print(name.upper())
    print("vous avez séléctinné : ")
    for pro,prix_uni in liste.items():
        print(f"{pro} : {prix_uni}€")
        
    print(f"Total {c}€")
    print()
    
    if c >= 200:
        print("20% de reduiction")
        print(f"Total {p}€")



for prod,prix in produits.items():
    print(f"{prod} : {prix} €")

print()
name = input("votre nom : ")
select1 = input("select produit 1 : ")
select2 = input("select produit 2 : ")
client(name, select1, select2)

    



    
    
    
        