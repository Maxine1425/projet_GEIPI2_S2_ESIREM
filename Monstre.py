import random


class Monstre:
    def __init__(self, name, rare, type):
        self.name = name
        self.rare = rare  # Niveau de raret� de 1 � 10
        self.type = type  # Type entre Attaque et Defense
        self.isKO = False # Est ce que le monstr est KO 
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

        self.initial_max_PV = self.PV

    def get_stats(self):  # Renvoie un tableau avec les stats du monstre
        stats = [self.name, "PV = " + str(self.PV), "ATQ = " + str(self.ATQ), "DEF = " + str(self.DEF), "VIT = " + str(self.VIT)]
        return stats

    def get_Pv(self):
        return self.PV

    def deal_damage(self, damage):
        damage = damage + 0.3 * self.DEF
        self.PV = self.PV - damage
        if self.PV < 0:
            self.PV = 0

    def choix_attaque(self, choice, opponent):
        if choice == 1:
            self.attaque(opponent)
        elif choice == 2:
            self.soin()

    def attaque(self, target):
        target.dealDamage(self.ATQ * 1.5)

    def soin(self):
        if self.PV + (self.initial_max_PV * 0.5) <= self.initial_max_PV:
            self.PV = self.PV + (self.initial_max_PV * 0.5)
        elif self.PV + (self.initial_max_PV * 0.5) > self.initial_max_PV:
            self.PV = self.initial_max_PV

    def ko_mon(self):
        self.isKO = True

    def rev_mon(self):
        self.isKO = False
