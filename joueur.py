from item import *
from pathlib import Path
import os
from argent import Compteur
from monstre import *
from item import *

class Joueur:

    def __init__(self, name, balance, mod, modp2, modp5, modp10):
        self.name = name
        self.portefeuille = Compteur()
        if balance != 0:
            self.portefeuille.compteur = balance
        self.portefeuille.mod = mod
        self.liste_mod = [modp2, modp5, modp10]
        self.liste_monstre = []  # Liste contenant tout les monstres que le joueur possède

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

        self.liste_epee = epee
        self.liste_bouclier = bouclier
        self.liste_bottes = bottes
        self.liste_soupe = soupe

        self.portefeuille.demarrer()

    def ajouter_item(self, item):
        if item.type == "epee" and self.liste_epee.rare == 0:
            self.liste_epee = item
            return 1
        elif item.type == "epee" and self.liste_epee.rare != 0:
            return 2

        elif item.type == "bouclier" and self.liste_bouclier.rare == 0:
            self.liste_bouclier = item
            return 1
        elif item.type == "bouclier" and self.liste_bouclier.rare != 0:
            return 2

        elif item.type == "bottes" and self.liste_bottes.rare == 0:
            self.liste_bottes = item
            return 1
        elif item.type == "bottes" and self.liste_bottes.rare != 0:
            return 2

        elif item.type == "soupe" and self.liste_soupe.rare == 0:
            self.liste_soupe = item
            return 1
        elif item.type == "soupe" and self.liste_soupe.rare != 0:
            return 2

        else:
            print("Type d'item invalide.")

    def supprimer_item(self, item):
        if item.type == "epee":
            self.liste_epee.rare = 0
            self.liste_epee.valeur_atq = 0
        elif item.type == "bouclier":
            self.liste_bouclier.rare = 0
            self.liste_bouclier.valeur_def = 0
        elif item.type == "bottes":
            self.liste_bottes.rare = 0
            self.liste_bottes.valeur_vit = 0
        elif item.type == "soupe":
            self.liste_soupe.rare = 0
            self.liste_soupe.valeur_pv = 0

    def get_items(self):
        return self.liste_soupe + self.liste_bottes + self.liste_epee + self.liste_bouclier

    def ajouter_monstre(self, monstre):  # Ajoute un monstre à l'inventaire de monstres du joueur
        try:
            length = len(self.liste_monstre)
            if length == 0:
                self.liste_monstre.append(monstre)
            elif length > 0 and length < 3:
                self.liste_monstre.insert(length, monstre)
        except:
            print("Une erreur est survenue.")

    def check_argent(self, montant):
        if self.portefeuille.compteur-montant >= 0:
            return True
        else:
            return False

    def ajouter_mod(self, valeur):
        self.portefeuille.ajouter_mod(valeur)

    def achat(self, montant):
        self.portefeuille.soustraire(montant)

    def vendre(self, montant):
        self.portefeuille.compteur += montant

    def print_nom_monstre(self):  # Affiche sur le terminal le nom de tout les monstres du joueur
        length = len(self.liste_monstre)
        for i in range(length):
            print(self.liste_monstre[i].name)

    import os

    def tout_sauvegarder(self):
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name
        os.makedirs(chemin_fichier_sauvegarde, exist_ok=True)
        self.sauvegarde_monstre(chemin_fichier_sauvegarde)
        self.sauvegarde_argent(chemin_fichier_sauvegarde)
        self.sauvegarde_items(chemin_fichier_sauvegarde)

    def sauvegarde_argent(self, chemin_fichier_sauvegarde):  # Sauvegarde l'argent et les mod du joueur dans un fichier nomdujoueur_money.txt
        nom_fichier = "argent.txt"
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name
        fichier_a_ouvrir = chemin_fichier_sauvegarde + "/" + nom_fichier
        donnee_argent = str(self.portefeuille.compteur) + "\n" + str(self.portefeuille.mod) + "\n" + str(self.liste_mod)
        with open(fichier_a_ouvrir, 'w') as current:
            current.write(donnee_argent)

    def sauvegarde_monstre(self, chemin_fichier_sauvegarde):  # Sauvegarde les monstres du joueur dans un fichier nomdujoueur_monster.txt
        nom_fichier = "monstre.txt"
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name
        fichier_a_ouvrir = chemin_fichier_sauvegarde + "/" + nom_fichier
        longueur = len(self.liste_monstre)
        with open(fichier_a_ouvrir, 'w') as current:
            for i in range(longueur):
                current.write(str(self.liste_monstre[i].nom))
                current.write("\n")
                current.write(str(self.liste_monstre[i].rare))
                current.write("\n")
                current.write(str(self.liste_monstre[i].type))
                current.write("\n")
                current.write(str(self.liste_monstre[i].PV))
                current.write("\n")
                current.write(str(self.liste_monstre[i].ATQ))
                current.write("\n")
                current.write(str(self.liste_monstre[i].DEF))
                current.write("\n")
                current.write(str(self.liste_monstre[i].VIT))
                current.write("\n")
                current.write(str(self.liste_monstre[i].chemin_image))
                current.write("\n")
                current.write("%\n")

    def sauvegarde_items(self, chemin_fichier_sauvegarde):
        nom_fichier = "item.txt"
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name
        fichier_a_ouvrir = chemin_fichier_sauvegarde + "/" + nom_fichier
        with open(fichier_a_ouvrir, 'w') as current:
                current.write("type = " + str(self.liste_epee.type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_epee.rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_epee.valeur_atq))
                current.write("\n")
                current.write("\n")

                current.write("-------------------------------")
                current.write("\n")
                current.write("type = " + str(self.liste_bouclier.type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_bouclier.rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_bouclier.valeur_def))
                current.write("\n")
                current.write("\n")

                current.write("-------------------------------")
                current.write("\n")

                current.write("type = " + str(self.liste_bottes.type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_bottes.rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_bottes.valeur_vit))
                current.write("\n")
                current.write("\n")

                current.write("-------------------------------")
                current.write("\n")

                current.write("type = " + str(self.liste_soupe.type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_soupe.rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_soupe.valeur_pv))
                current.write("\n")
                current.write("\n")

                current.write("\n")

    def charger_joueur(self, name):
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + name

        # Charger l'argent
        fichier_argent = chemin_fichier_sauvegarde + "/argent.txt"
        with open(fichier_argent, 'r') as f:
            compteur = int(f.readline())
            mod = int(f.readline())
            liste_mod = eval(f.readline())

        # Charger les monstres
        fichier_monstre = chemin_fichier_sauvegarde + "/monstre.txt"
        liste_monstre = []
        with open(fichier_monstre, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                nom = lines[i].strip()
                rare = lines[i + 1].strip()
                type = lines[i + 2].strip()
                chemin_image = lines[i + 8].strip()
                monstre = Monstre(nom=nom, rare=rare, type=type, chemin_image=chemin_image)
                monstre.PV = int(lines[i + 3])
                monstre.ATQ = int(lines[i + 4])
                monstre.DEF = int(lines[i + 5])
                monstre.VIT = int(lines[i + 6])
                monstre.initial_max_PV = monstre.PV
                liste_monstre.append(monstre)
                i += 9

        # Charger les items
        fichier_items = chemin_fichier_sauvegarde + "/item.txt"
        liste_epee = []
        liste_bouclier = []
        liste_bottes = []
        liste_soupe = []
        with open(fichier_items, 'r') as f:
            lines = f.readlines()
            item_type = None
            for line in lines:
                if "type =" in line:
                    item_type = line.split('=')[1].strip()
                elif "rarete =" in line:
                    rarete = line.split('=')[1].strip()
                elif "valeur =" in line:
                    valeur = line.split('=')[1].strip()

                    # Créer l'item approprié
                    if item_type == "epee":
                        item = Item(rare=rarete, type=item_type)
                        item.valeur_atq = valeur
                    elif item_type == "bouclier":
                        item = Item(rare=rarete, type=item_type)
                        item.valeur_def = valeur
                    elif item_type == "bottes":
                        item = Item(rare=rarete, type=item_type, )
                        item.valeur_vit = valeur
                    elif item_type == "soupe":
                        item = Item(rare=rarete, type=item_type, )
                        item.valeur_pv = valeur

                    # Ajouter l'item à la liste appropriée
                    if item_type == "epee":
                        liste_epee.append(item)
                    elif item_type == "bouclier":
                        liste_bouclier.append(item)
                    elif item_type == "bottes":
                        liste_bottes.append(item)
                    elif item_type == "soupe":
                        liste_soupe.append(item)

        self.portefeuille.compteur = compteur
        self.portefeuille.mod = mod
        self.liste_mod = liste_mod

        self.liste_monstre = liste_monstre
        self.liste_epee = liste_epee
        self.liste_bouclier = liste_bouclier
        self.liste_bottes = liste_bottes
        self.liste_soupe = liste_soupe