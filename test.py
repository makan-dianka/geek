class Pecheur:
    def __init__(self, poison):
        self.name = poison
        self.montant = 2000
        self.point_depart = 1500
        self.saumon = 100
        self.courbine = 50
        self.espadon = 30
        self.kilo = 5
        

    def get_saumon(self):
        return self.point_depart - self.saumon
    
    def get_courbine(self):
        return self.point_depart - self.courbine
    
    def get_espadon(self):
        return self.point_depart - self.espadon
    
    
    def point_restant(self, poison, kilo):
        if Pecheur(poison).name == "saumon":
            self.kilo *= kilo
            saumon = self.get_saumon() - self.kilo
            somme = self.montant - saumon
            print(f"Vous avez pêché [Saumon]\nKilo pêché : {kilo}\nPoint perdu kilo: {self.kilo}\nPoint restant : {saumon}\nDebouser : {somme} MAD")
        elif Pecheur(poison).name == "courbine":
            self.kilo *= kilo
            courbine = self.get_courbine() - self.kilo
            somme = self.montant - courbine
            print(f"Vous avez pêché [Courbine]\nKilo pêché : {kilo}\nPoint perdu kilo: {self.kilo}\nPoint restant : {courbine}\nDebouser : {somme} MAD")
        elif Pecheur(poison).name == "espadon":
            self.kilo *= kilo
            espadon = self.get_espadon() - self.kilo
            somme = self.montant - espadon
            print(f"Vous avez pêché [Espadon]\nKilo pêché : {kilo}\nPoint perdu kilo: {self.kilo}\nPoint restant : {espadon}\nDebouser : {somme} MAD")
        else:
            print("Oups ! vous devez saisir un type de poison.")
            
    
print(
    "Les options : [Saumon, Courbine, Espadon]"
    )        
poison = input("Qu'avez-vous pêché ? \n>> ")
try:
    kilo = int(input(f"Combien de kilo de {poison} avez-vous pêché ?\n>> "))
except:
    print("Kilo est un entier : ex 1, 2, 3, 4 etc.")
else:
    poison = poison.lower()
    obj = Pecheur(poison)
    obj.point_restant(obj.name, kilo)
    
    
    