import random


class Monstre:
    def __init__(self, name, rare, type):
        self.name = name
        self.rare = rare
        self.type = type
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


    def get_stats(self):
        stats = [self.name, self.PV, self.ATQ, self.DEF, self.VIT]
        return stats

    def print_stats(self):
        print(self.name, self.rare, self.type, self.PV, self.ATQ, self.DEF, self.VIT)