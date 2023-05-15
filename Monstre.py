import random
class Monstre:
    def __init__(self, name, rare, type):
        self.name = name
        self.rare = rare #Niveau de rareté de 1 à 10
        self.type = type #Type entre Attaque et Defense
        if type == "Attaque":
            self.PV = random.randint(10, 60)
            self.ATQ = random.randint(25, 40)
            self.DEF = random.randint(1, 15)
            self.VIT = random.randint(1, 15)


        elif type == "Defense":
            self.PV = random.randint(50, 100)
            self.ATQ = random.randint(1, 15)
            self.DEF = random.randint(15, 30)
            self.VIT = random.randint(1, 15)


    def get_stats(self): #Renvoie un tableau avec les stats du monstre
        stats = [self.name, self.PV, self.ATQ, self.DEF, self.VIT]
        return stats
