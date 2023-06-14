from pathlib import Path
import os
from Money import Compteur

class Player:

    def __init__(self, name, balance, mod, modp2, modp5, modp10):
        self.name = name
        self.wallet = Compteur()
        if balance != 0:
            self.wallet.compteur = balance
        self.wallet.mod = mod
        self.mod_list = [ modp2, modp5, modp10]
        self.monster_list = []  # Liste contenant tout les monstres que le joueur poss�de

        self.liste_epee = []
        self.liste_bouclier = []
        self.liste_bottes = []
        self.liste_soupe = []

        self.wallet.demarrer()

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
            print("trop d'�p�e")
        elif item.type == "bouclier":
            self.liste_bouclier.append(item)
        elif item.type == "bottes":
            self.liste_bottes.append(item)
        elif item.type == "soupe":
            self.liste_soupe.append(item)
        else:
            print("Invalid item type")

    def get_items(self):
        return self.liste_soupe + self.liste_bottes + self.liste_epee + self.liste_bouclier

    def add_monstre(self, monstre):  # Ajoute un monstre � l'inventaire de monstres du joueur
        try:
            length = len(self.monster_list)
            if length == 0:
                self.monster_list.append(monstre)
            else:
                self.monster_list.insert(length, monstre)
        except:
            print("An error has occurred")


    def check_argent(self, montant):
        if self.wallet.compteur-montant >= 0:
            return True
        else:
            return False
    def ajouter_mod(self, valeur):
        self.wallet.ajouter_mod(valeur)

    def achat(self, montant):
        self.wallet.soustraire(montant)
    def print_monster_name(self):  # Affiche sur le terminal le nom de tout les monstres du joueur
        length = len(self.monster_list)
        for i in range(length):
            print(self.monster_list[i].name)

    def save_all(self):
        self.sauvegarde_monstre()
        self.sauvegarde_argent()


    def commencer_combat(self, adversaire):
        joueur = self.monster_list[0]

    def sauvegarde_argent(self):  # Sauvegarde l'argent et les mod du joueur dans un fichier nomdujoueur_money.txt
        file_name = self.name + "_money.txt"
        save_folder_path = "save files/" + self.name
        file_to_open = save_folder_path + "/" + file_name
        money_data = str(self.wallet.compteur) + "\n" + str(self.wallet.mod) + "\n" + str(self.mod_list)
        with open(file_to_open, 'w') as current:
            current.write(money_data)

    def sauvegarde_monstre(self):  # Sauvegarde les monstres du joueur dans un fichier nomdujoueur_monster.txt
        file_name = self.name + "_monster.txt"
        save_folder = Path("save files/")

        try:
            path = os.path.join(save_folder, self.name)
            os.mkdir(path)
            print("File created!\n")
        except:
            print("File already exists !\n")

        file_to_open = save_folder / self.name / file_name
        length = len(self.monster_list)
        with open(file_to_open, 'w') as current:
            for i in range(length):
                current.write(str(self.monster_list[i].name))
                current.write("\n")
                current.write(str(self.monster_list[i].rare))
                current.write("\n")
                current.write(str(self.monster_list[i].type))
                current.write("\n")
                current.write(str(self.monster_list[i].PV))
                current.write("\n")
                current.write(str(self.monster_list[i].ATQ))
                current.write("\n")
                current.write(str(self.monster_list[i].DEF))
                current.write("\n")
                current.write(str(self.monster_list[i].VIT))
                current.write("\n")
                current.write("%\n")

    def sauvegarde_items(self):
        file_name = self.name + "_items.txt"
        save_folder = Path("save files/")

        try:
            path = os.path.join(save_folder, self.name)
            os.mkdir(path)
            print("File created!\n")
        except:
            print("File already exists !\n")

        file_to_open = save_folder / self.name / file_name
        length = len(self.monster_list)
        with open(file_to_open, 'w') as current:
            for i in range(length):
                current.write(str(self.item[i].type))
                current.write("\n")
                current.write(str(self.item[i].valeur_atq))
                current.write("\n")
                current.write(str(self.item[i].valeur_pv))
                current.write("\n")
                current.write(str(self.item[i].valeur_def))
                current.write("\n")
                current.write(str(self.item[i].valeur_vit))
                current.write("\n")

