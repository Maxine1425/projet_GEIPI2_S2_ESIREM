import random
class Monstre:
    def __init__(self, name, rare, type):
        self.name = name
        self.rare = rare
        self.type = type
        if type == "Attaque":
            self.ATQ = random.randint(25, 40)
            self.DEF = random.randint(1, 15)
            self.VIT = random.randint(1, 15)
            self.PV = random.randint(10, 60)

        elif type == "Defense":
            self.ATQ = random.randint(1, 15)
            self.DEF = random.randint(15, 30)
            self.VIT = random.randint(1, 15)
            self.PV = random.randint(50, 100)


    # def show_stats(self):
    #     atq = str(self.ATQ)
    #     def = str(self.DEF)
    #     vit = str(self.VIT)
    #     pv = str(self.PV)
    #
    #     stats = str(self.name + "\nPV = " + pv + "\nATQ = " + atq + "\nDEF = " + def + )
    #     return stats
