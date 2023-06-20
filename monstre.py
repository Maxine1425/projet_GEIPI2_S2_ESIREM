import random
from item import *


class Monstre:
    def __init__(self):
        # Choix d'un nom aleatoire parmis la liste des 10 monstres.
        liste_nom = ["Crolite", "Wallabic", "Panthoal", "Crocodithe", "Whirlling", "Skeleroach", "Demeton", "Silverilla", "Pyrose", "Vaporc" ]
        self.nom = random.choice(liste_nom)
        if self.nom == "Crolite":
            self.rare = 1  # Niveau de rarete de 1 à 5
            self.type = "Attaque"  # Type entre Attaque et Defense
            self.chemin_image = "images/Crolite.png"  # Chemin vers l'image du monstre

        elif self.nom == "Wallabic":
            self.rare = 2  # Niveau de rarete de 1 à 5
            self.type = "Attaque"  # Type entre Attaque et Defense
            self.chemin_image = "images/Wallabic.png"  # Chemin vers l'image du monstre

        elif self.nom == "Panthoal":
            self.rare = 3  # Niveau de rarete de 1 à 5
            self.type = "Attaque"  # Type entre Attaque et Defense
            self.chemin_image = "images/Panthoal.png"  # Chemin vers l'image du monstre

        elif self.nom == "Crocodithe":
            self.rare = 4  # Niveau de rarete de 1 à 5
            self.type = "Attaque"  # Type entre Attaque et Defense
            self.chemin_image = "images/Crocodithe.png"  # Chemin vers l'image du monstre

        elif self.nom == "Whirlling":
            self.rare = 5  # Niveau de rarete de 1 à 5
            self.type = "Attaque"  # Type entre Attaque et Defense
            self.chemin_image = "images/Whirlling.png"  # Chemin vers l'image du monstre

        elif self.nom == "Skeleroach":
            self.rare = 1  # Niveau de rarete de 1 à 5
            self.type = "Defense"  # Type entre Attaque et Defense
            self.chemin_image = "images/Skeleroach.png"  # Chemin vers l'image du monstre

        elif self.nom == "Demeton":
            self.rare = 2  # Niveau de rarete de 1 à 5
            self.type = "Defense"  # Type entre Attaque et Defense
            self.chemin_image = "images/Demeton.png"  # Chemin vers l'image du monstre

        elif self.nom == "Silverilla":
            self.rare = 3  # Niveau de rarete de 1 à 5
            self.type = "Defense"  # Type entre Attaque et Defense
            self.chemin_image = "images/Silverilla.png"  # Chemin vers l'image du monstre

        elif self.nom == "Pyrose":
            self.rare = 4  # Niveau de rarete de 1 à 5
            self.type = "Defense"  # Type entre Attaque et Defense
            self.chemin_image = "images/Pyrose.png"  # Chemin vers l'image du monstre

        elif self.nom == "Vaporc":
            self.rare = 5  # Niveau de rarete de 1 à 5
            self.type = "Defense"  # Type entre Attaque et Defense
            self.chemin_image = "images/Vaporc.png"  # Chemin vers l'image du monstre

        self.est_ko = False  # Est-ce que le monstre est KO
        self.choice = 1 # Choix du monstre durant le combat, de base a 1

        # Meme probleme que dans Joueur, et meme solution que dans Joueur.
        epee = Item(1, "epee")
        bouclier = Item(1, "bouclier")
        bottes = Item(1, "bottes")
        soupe = Item(1, "soupe")

        epee.rare = 0
        epee.valeur_atq = 0

        bouclier.rare = 0
        bouclier.valeur_def = 0

        bottes.rare = 0
        bottes.valeur_vit = 0

        soupe.rare = 0
        soupe.valeur_pv = 0

        self.item_equipe_epee = epee
        self.item_equipe_bouclier = bouclier
        self.item_equipe_bottes = bottes
        self.item_equipe_soupe = soupe

        # Definition des statistiques selon la rarete et le type.
        if self.rare == 1:
            if self.type == "Attaque":
                self.PV = random.randint(100, 200)
                self.ATQ = random.randint(50, 150)
                self.DEF = random.randint(1, 15)
                self.VIT = random.randint(1, 15)
            elif self.type == "Defense":
                self.PV = random.randint(250, 400)
                self.ATQ = random.randint(1, 50)
                self.DEF = random.randint(20, 50)
                self.VIT = random.randint(1, 10)

        if self.rare == 2:
            if self.type == "Attaque":
                self.PV = random.randint(200, 400)
                self.ATQ = random.randint(100, 300)
                self.DEF = random.randint(2, 30)
                self.VIT = random.randint(1, 15)
            elif self.type == "Defense":
                self.PV = random.randint(500, 800)
                self.ATQ = random.randint(2, 100)
                self.DEF = random.randint(40, 100)
                self.VIT = random.randint(1, 10)

        if self.rare == 3:
            if self.type == "Attaque":
                self.PV = random.randint(300, 600)
                self.ATQ = random.randint(150, 450)
                self.DEF = random.randint(3, 45)
                self.VIT = random.randint(1, 15)
            elif self.type == "Defense":
                self.PV = random.randint(750, 1200)
                self.ATQ = random.randint(3, 150)
                self.DEF = random.randint(60, 150)
                self.VIT = random.randint(1, 10)

        if self.rare == 4:
            if self.type == "Attaque":
                self.PV = random.randint(400, 800)
                self.ATQ = random.randint(200, 600)
                self.DEF = random.randint(4, 60)
                self.VIT = random.randint(1, 15)
            elif self.type == "Defense":
                self.PV = random.randint(1000, 1600)
                self.ATQ = random.randint(4, 60)
                self.DEF = random.randint(80, 200)
                self.VIT = random.randint(1, 10)

        if self.rare == 5:
            if self.type == "Attaque":
                self.PV = random.randint(500, 1000)
                self.ATQ = random.randint(250, 750)
                self.DEF = random.randint(5, 75)
                self.VIT = random.randint(1, 15)
            elif self.type == "Defense":
                self.PV = random.randint(1250, 2000)
                self.ATQ = random.randint(5, 250)
                self.DEF = random.randint(100, 220)
                self.VIT = random.randint(1, 10)

        self.initial_max_PV = self.PV

    def deal_damage(self, damage):
        """
        Fait des degats sur une cible.
        :param damage: degats a faire
        """
        damage = damage + 0.3 * self.DEF
        self.PV = self.PV - damage
        if self.PV < 0:
            self.PV = 0

    def choix_attaque(self, opponent):
        """
        execute une attaque ou un soin selon le choix du monstre.
        :param opponent: Adversaire sur lequel taper si on choisit d'attaquer.
        """
        if self.choice == 1:
            self.attaque(opponent)
        elif self.choice == 2:
            self.soin()

    def attaque(self, target):
        target.deal_damage(self.ATQ * 1.5)

    def soin(self):
        if self.PV + (self.initial_max_PV * 0.5) <= self.initial_max_PV:
            self.PV = self.PV + (self.initial_max_PV * 0.5)
        elif self.PV + (self.initial_max_PV * 0.5) > self.initial_max_PV:
            self.PV = self.initial_max_PV

    def ko_mon(self):
        """
        Met un monstre KO
        """
        self.isKO = True

    def rev_mon(self):
        """
        Revive un monstre.
        """
        self.isKO = False

    def bouger_item_monstre(self, prochain_monstre):
        """
        Echange les objets d'un monstre avec un autre
        :param prochain_monstre: Monstre avec lesquels echanger les objets du monstre actuel.
        """
        temp_epee = self.item_equipe_epee
        temp_bouclier = self.item_equipe_bouclier
        temp_bottes = self.item_equipe_bottes
        temp_soupe = self.item_equipe_soupe

        self.retirer_item_monstre(self.item_equipe_epee)
        self.retirer_item_monstre(self.item_equipe_bouclier)
        self.retirer_item_monstre(self.item_equipe_bottes)
        self.retirer_item_monstre(self.item_equipe_soupe)

        prochain_monstre.modifier_item_monstre(temp_epee)
        prochain_monstre.modifier_item_monstre(temp_bouclier)
        prochain_monstre.modifier_item_monstre(temp_bottes)
        prochain_monstre.modifier_item_monstre(temp_soupe)

    def modifier_stat_monstre(self):
        """
        Met a jour les stats du monstre selon les items equipes
        """
        self.ATQ += self.item_equipe_epee.valeur_atq
        self.DEF += self.item_equipe_bouclier.valeur_def
        self.VIT += self.item_equipe_bottes.valeur_vit
        self.PV += self.item_equipe_soupe.valeur_pv

    def modifier_item_monstre(self, item):
        """
        Ajoute un item au monstre
        :param item: Item a ajouter.
        """
        if item.type == "epee":
            self.item_equipe_epee = item
        if item.type == "bouclier":
            self.item_equipe_bouclier = item
        if item.type == "bottes":
            self.item_equipe_bottes = item
        if item.type == "soupe":
            self.item_equipe_soupe = item
        # On met a jour les stast du monstre a chaque objet ajoute
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
        """
        Sous classes permettant d'optimiser la creation des monstres, elles ne sont pas utilisees pour l'instant mais
        pourraient l'etre dans le futur
        """
        PV = random.randint(100, 600)
        ATQ = random.randint(100, 160)
        DEF = random.randint(1, 15)
        VIT = random.randint(1, 15)
        return PV, ATQ, DEF, VIT


class MonstreDefense(Monstre):
    def define_stats(self):
        """
        Sous classes permettant d'optimiser la creation des monstres, elles ne sont pas utilisees pour l'instant mais
        pourraient l'etre dans le futur
        """
        PV = random.randint(500, 1000)
        ATQ = random.randint(4, 60)
        DEF = random.randint(15, 30)
        VIT = random.randint(1, 15)
        return PV, ATQ, DEF, VIT
