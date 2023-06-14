from pathlib import Path
import os
from argent import Compteur

class Joueur:

    def __init__(self, name, balance, mod, modp2, modp5, modp10):
        self.name = name
        self.portefeuille = Compteur()
        if balance != 0:
            self.portefeuille.compteur = balance
        self.portefeuille.mod = mod
        self.liste_mod = [modp2, modp5, modp10]
        self.liste_monstre = []  # Liste contenant tout les monstres que le joueur possède

        self.liste_epee = []
        self.liste_bouclier = []
        self.liste_bottes = []
        self.liste_soupe = []

        self.portefeuille.demarrer()

    def get_nombre_epee(self):
        return len(self.liste_epee)

    def get_nombre_bouclier(self):
        return len(self.liste_bouclier)

    def get_nombre_bottes(self):
        return len(self.liste_bottes)

    def get_nombre_soupe(self):
        return len(self.liste_soupe)

    def ajouter_item(self, item):
        if item.type == "epee" and len(self.liste_epee) <= 3:
            self.liste_epee.append(item)
        elif item.type == "epee" and len(self.liste_epee) > 3:
            print("trop d'epee")
        elif item.type == "bouclier":
            self.liste_bouclier.append(item)
        elif item.type == "bottes":
            self.liste_bottes.append(item)
        elif item.type == "soupe":
            self.liste_soupe.append(item)
        else:
            print("Type d'item invalide.")

    def get_items(self):
        return self.liste_soupe + self.liste_bottes + self.liste_epee + self.liste_bouclier

    def ajouter_monstre(self, monstre):  # Ajoute un monstre à l'inventaire de monstres du joueur
        try:
            length = len(self.liste_monstre)
            if length == 0:
                self.liste_monstre.append(monstre)
            else:
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
                current.write("%\n")

    def sauvegarde_items(self, chemin_fichier_sauvegarde):
        nom_fichier = "item.txt"
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name
        fichier_a_ouvrir = chemin_fichier_sauvegarde + "/" + nom_fichier
        longueur = len(self.liste_epee)
        with open(fichier_a_ouvrir, 'w') as current:
            for i in range(longueur):
                current.write("type = " + str(self.liste_epee[i].type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_epee[i].rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_epee[i].valeur_atq))
                current.write("\n")
                current.write("\n")

            current.write("-------------------------------")
            current.write("\n")
            longueur = len(self.liste_bouclier)
            for i in range(longueur):
                current.write("type = " + str(self.liste_bouclier[i].type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_bouclier[i].rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_bouclier[i].valeur_def))
                current.write("\n")
                current.write("\n")

            current.write("-------------------------------")
            current.write("\n")
            longueur = len(self.liste_bottes)
            for i in range(longueur):
                current.write("type = " + str(self.liste_bottes[i].type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_bottes[i].rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_bottes[i].valeur_vit))
                current.write("\n")
                current.write("\n")

            current.write("-------------------------------")
            current.write("\n")
            longueur = len(self.liste_soupe)
            for i in range(longueur):
                current.write("type = " + str(self.liste_soupe[i].type))
                current.write("\n")
                current.write("rarete = " + str(self.liste_soupe[i].rare))
                current.write("\n")
                current.write("valeur = " + str(self.liste_soupe[i].valeur_pv))
                current.write("\n")
                current.write("\n")

            current.write("\n")
