import random
from item import *

class Monstre:
    def __init__(self, nom, rare, type, chemin_image):
        self.nom = nom
        self.rare = rare  # Niveau de rarete de 1 à 10
        self.type = type  # Type entre Attaque et Defense
        self.est_ko = False  # Est-ce que le monstre est KO
        self.chemin_image = chemin_image  # Chemin vers l'image du monstre
        self.choice = 1
        self.item_equipe_epee = 0
        self.item_equipe_bouclier = 0
        self.item_equipe_bottes = 0
        self.item_equipe_soupe = 0

        if type == "Attaque":
            self.PV = random.randint(100, 600)
            self.ATQ = random.randint(100, 160)
            self.DEF = random.randint(1, 15)
            self.VIT = random.randint(1, 15)
        elif type == "Defense":
            self.PV = random.randint(500, 1000)
            self.ATQ = random.randint(4, 60)
            self.DEF = random.randint(15, 30)
            self.VIT = random.randint(1, 15)

        self.initial_max_PV = self.PV

    def get_stats(self):  # Renvoie un tableau avec les stats du monstre
        stats = [self.nom, "PV = " + str(self.PV), "ATQ = " + str(self.ATQ), "DEF = " + str(self.DEF),
                 "VIT = " + str(self.VIT)]
        return stats

    def get_Pv(self):
        return self.PV

    def deal_damage(self, damage):
        damage = damage + 0.3 * self.DEF
        self.PV = self.PV - damage
        if self.PV < 0:
            self.PV = 0

    def choix_attaque(self, opponent):
        if self.choice == 1:
            self.attaque(opponent)
        elif self.choice == 2:
            self.soin()
            print("SOIN OK")

    def attaque(self, target):
        target.deal_damage(self.ATQ * 1.5)

    def soin(self):
        if self.PV + (self.initial_max_PV * 0.5) <= self.initial_max_PV:
            self.PV = self.PV + (self.initial_max_PV * 0.5)
        elif self.PV + (self.initial_max_PV * 0.5) > self.initial_max_PV:
            self.PV = self.initial_max_PV

    def ko_mon(self):
        self.isKO = True

    def rev_mon(self):
        self.isKO = False

    def modifier_stat_monstre(self):
        self.ATQ += self.item_equipe_epee.valeur_atq
        self.DEF += self.item_equipe_bouclier.valeut_def
        self.VIT += self.item_equipe_bottes.valeur_vit
        self.PV += self.item_equipe_soupe.valeut_pv
    def modifier_item_monstre(self, item):
        if item.type == "epee":
            self.item_equipe_epee = item
        if item.type == "bouclier":
            self.item_equipe_bouclier = item
        if item.type == "bottes":
            self.item_equipe_bottes = item
        if item.type == "soupe":
            self.item_equipe_soupe = item
        self.modifier_stat_monstre()

    def retirer_item_monstre(self, item):
        if item.type == "epee":
            self.item_equipe_epee = 0
        if item.type == "bouclier":
            self.item_equipe_bouclier = 0
        if item.type == "bottes":
            self.item_equipe_bottes = 0
        if item.type == "soupe":
            self.item_equipe_soupe = 0
        self.modifier_stat_monstre()

class MonstreAttaque(Monstre):
    def define_stats(self):
        PV = random.randint(100, 600)
        ATQ = random.randint(100, 160)
        DEF = random.randint(1, 15)
        VIT = random.randint(1, 15)
        return PV, ATQ, DEF, VIT


class MonstreDefense(Monstre):
    def define_stats(self):
        PV = random.randint(500, 1000)
        ATQ = random.randint(4, 60)
        DEF = random.randint(15, 30)
        VIT = random.randint(1, 15)
        return PV, ATQ, DEF, VIT
