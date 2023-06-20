from item import *
from pathlib import Path
import os
from argent import Compteur
from monstre import *
from item import *


class Joueur:

    def __init__(self, name, balance, mod, modp2, modp5, modp10):
        """
        :param name: Nom du joueur
        :param balance: argent du joueur
        :param mod: combien le joueur gagne par seconde
        :param modp2: nombre de modificateurs 2 que le joueur a
        :param modp5: nombre de modificateurs 5 que le joueur a
        :param modp10: nombre de modificateurs 10 que le joueur a
        """
        self.name = name
        # On commence un thread pour garder une trace de l'argent du joueur.
        self.portefeuille = Compteur()
        if balance != 0:
            self.portefeuille.compteur = balance
        self.portefeuille.mod = mod
        self.liste_mod = [modp2, modp5, modp10]

        # Le fait que le joueur n'ai pas de monstre posait probleme, on a donc simule ce procede en lui donnant des
        # des monstres avec comme rarete 0 et comme image une image indiquant qu'il n'y a pas de monstre.z
        monstre1 = Monstre()
        monstre2 = Monstre()
        monstre3 = Monstre()

        monstre1.rare = 0
        monstre2.rare = 0
        monstre3.rare = 0

        monstre1.chemin_image = "images/pas_de_monstre.png"
        monstre2.chemin_image = "images/pas_de_monstre.png"
        monstre3.chemin_image = "images/pas_de_monstre.png"

        self.liste_monstre = [monstre1, monstre2, monstre3]  # Liste contenant tout les monstres que le joueur possède,
                                                             # Il ne peut pas avoir plus de 3 monstres.

        # Meme probleme que pour la liste monstre.
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

        # Attribut pour garder une trace de la collection du joueur, c'est à dire quels monstres il a deja eu.
        self.collection_monstre = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Debut du thread.
        self.portefeuille.demarrer()

    def nombre_monstre_collection(self):
        """
        :return: Le nombre de monstres que le joueur a deja eu.
        """
        compteur = 0
        length = len(self.collection_monstre)
        for i in range(length):
            if self.collection_monstre[i] == 1:
                compteur += 1
        return compteur

    def ajouter_collection(self, nom_monstre):
        """
        Fonction permettant de checker si le joueur a deja eu un monstre, et si non, lui ajoute a sa collection.
        :param nom_monstre: nom du monstre que le joueur viens d'obtenir
        """
        if nom_monstre == "Crolite":
            if self.collection_monstre[0] == 0:
                self.collection_monstre[0] = 1

        elif nom_monstre == "Wallabic":
            if self.collection_monstre[1] == 0:
                self.collection_monstre[1] = 1

        elif nom_monstre == "Panthoal":
            if self.collection_monstre[2] == 0:
                self.collection_monstre[2] = 1

        elif nom_monstre == "Crocodithe":
            if self.collection_monstre[3] == 0:
                self.collection_monstre[3] = 1

        elif nom_monstre == "Whirlling":
            if self.collection_monstre[4] == 0:
                self.collection_monstre[4] = 1

        elif nom_monstre == "Skeleroach":
            if self.collection_monstre[5] == 0:
                self.collection_monstre[5] = 1

        elif nom_monstre == "Demeton":
            if self.collection_monstre[6] == 0:
                self.collection_monstre[6] = 1

        elif nom_monstre == "Silverilla":
            if self.collection_monstre[7] == 0:
                self.collection_monstre[7] = 1

        elif nom_monstre == "Pyrose":
            if self.collection_monstre[8] == 0:
                self.collection_monstre[8] = 1

        elif nom_monstre == "Vaporc":
            if self.collection_monstre[9] == 0:
                self.collection_monstre[9] = 1

    def ajouter_item(self, item):
        """
        Fonction ajoutant un objet a la liste d'objets du joueur.
        :param item: Objet a ajouter.
        :return: 1 si l'objet a bien ete ajoute, 2 sinon.
        """
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
        """
        Supprime l'item donne de la liste d'items du joueur.
        :param item: item a supprim
        """
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

    def ajouter_monstre(self, monstre):
        """
        Ajoute un monstre a la liste de monstre du joueur.
        :param monstre: Monstre a ajouter.
        :return: 1 si le monstre a bien ete ajoute, 2 sinon.
        """
        # Check si l'image du monstre est l'image pas de monstre.
        if self.liste_monstre[0].chemin_image == "images/pas_de_monstre.png":
            self.liste_monstre[0] = monstre
            return 1
        elif self.liste_monstre[1].chemin_image == "images/pas_de_monstre.png":
            self.liste_monstre[1] = monstre
            return 1
        elif self.liste_monstre[2].chemin_image == "images/pas_de_monstre.png":
            self.liste_monstre[2] = monstre
            return 1
        else:
            return 2

    def bouger_monstre(self, emplacement):
        """
        Bouge le monstre a l'emplacement choisi a la place du premier monstre, et bouge le premier a l'emplacement
        choisi.
        :param emplacement: Emplacement du monstre a echanger.
        """
        temp = self.liste_monstre[0]
        self.liste_monstre[0] = self.liste_monstre[emplacement]
        self.liste_monstre[emplacement] = temp

    def retirer_monstre(self, emplacement):
        """
        Fonction retirant un monstre de la liste de monstre du joueur.
        Il faut noter que on ne lui enleve pas reellement, mais que l'on met juste toutes ses stats a des
        valeurs nulles.
        :param emplacement: Emplacement du monstre a retirer.
        """
        self.liste_monstre[emplacement].chemin_image = "images/pas_de_monstre.png"
        self.liste_monstre[emplacement].rare = 0
        self.liste_monstre[emplacement].nom = ""
        self.liste_monstre[emplacement].type = ""

    def check_argent(self, montant):
        """
        Check si le joueur a assez d'argent pour qu'on supprime le montant donne a sa fortune.
        :param montant: Montant a supprimer.
        :return: True si le montant peut etre enleve, False sinon.
        """
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

    def tout_sauvegarder(self):
        """
        Cree un dossier de sauvegarde pour le joueur si il n'en a pas deja un, puis executes toutes les fonctions
        de sauvegarde dans ce fichier.
        """
        try:
            chemin_base = "fichiers de sauvegarde"
            chemin_fichier_sauvegarde = os.path.join(chemin_base, self.name)
            if not os.path.exists(chemin_fichier_sauvegarde):
                os.makedirs(chemin_fichier_sauvegarde, exist_ok=True)
            self.sauvegarde_monstre(chemin_fichier_sauvegarde)
            self.sauvegarde_argent(chemin_fichier_sauvegarde)
            self.sauvegarde_items(chemin_fichier_sauvegarde)

        # Pour eviter que le programme ne crash
        except Exception as e:
            print("Une exception a ete levee:", e)

    def sauvegarde_argent(self, chemin_fichier_sauvegarde):
        """
        Sauvegarde les donnees relatives a l'argent du joueur dans un fichier argent.txt
        :param chemin_fichier_sauvegarde: chemin du fichier de sauvegarde
        """
        nom_fichier = "argent.txt"
        fichier_a_ouvrir = os.path.join(chemin_fichier_sauvegarde, nom_fichier)
        donnee_argent = str(self.portefeuille.compteur) + "\n" + str(self.portefeuille.mod) + "\n" + str(self.liste_mod)
        with open(fichier_a_ouvrir, 'w') as current:
            current.write(donnee_argent)
        pass

    def sauvegarde_monstre(self, chemin_fichier_sauvegarde):
        """
        Sauvegarde les monstres du joueur dans un fichier monstre.txt
        :param chemin_fichier_sauvegarde: chemin du fichier de sauvegarde
        :return:
        """
        nom_fichier = "monstre.txt"
        fichier_a_ouvrir = os.path.join(chemin_fichier_sauvegarde, nom_fichier)
        longueur = len(self.liste_monstre)
        with open(fichier_a_ouvrir, 'w') as current:
            for i in range(longueur):
                current.write(str(self.liste_monstre[i].nom))
                current.write("\n")
                current.write(str(self.liste_monstre[i].rare))
                current.write("\n")
                current.write(str(self.liste_monstre[i].type))
                current.write("\n")
                current.write(str(round(self.liste_monstre[i].PV, 2)))
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
        pass

    def sauvegarde_items(self, chemin_fichier_sauvegarde):
        """
        Sauvegarde les objets du joueur dans un fichier item.txt
        :param chemin_fichier_sauvegarde: chemin du fichier de sauvegarde
        """
        nom_fichier = "item.txt"
        fichier_a_ouvrir = os.path.join(chemin_fichier_sauvegarde, nom_fichier)
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
        pass

    def charger_joueur(self):
        """
        Fonction permettant de charger les donnees contenues dans les fichiers .txt, et d'overwrite les donnees
        actuelles du joueurs avec celle-ci.
        """
        chemin_fichier_sauvegarde = "fichiers de sauvegarde/" + self.name

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
                monstre = Monstre()
                monstre.nom = lines[i].strip()
                monstre.rare = lines[i + 1].strip()
                monstre.type = lines[i + 2].strip()
                monstre.PV = round(int(lines[i + 3]))
                monstre.ATQ = int(lines[i + 4])
                monstre.DEF = int(lines[i + 5])
                monstre.VIT = int(lines[i + 6])
                monstre.chemin_image = str(lines[i + 7].strip())
                monstre.initial_max_PV = monstre.PV
                liste_monstre.append(monstre)
                i += 9

        # Charger les items
        fichier_items = chemin_fichier_sauvegarde + "/item.txt"
        liste_epee = 0
        liste_bouclier = 0
        liste_bottes = 0
        liste_soupe = 0
        with open(fichier_items, 'r') as f:
            lines = f.readlines()
            item_type = None
            for line in lines:
                if "type =" in line:
                    item_type = line.split('=')[1].strip()
                elif "rarete =" in line:
                    rarete = int(line.split('=')[1].strip())
                elif "valeur =" in line:
                    valeur = int(line.split('=')[1].strip())

                    # Creer l'item approprie
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

                    # Ajouter l'item à la liste appropriee
                    if item_type == "epee":
                        liste_epee = item
                    elif item_type == "bouclier":
                        liste_bouclier = item
                    elif item_type == "bottes":
                        liste_bottes = item
                    elif item_type == "soupe":
                        liste_soupe = item

        self.portefeuille.compteur = compteur
        self.portefeuille.mod = mod
        self.liste_mod = liste_mod

        self.liste_monstre = liste_monstre
        self.liste_epee = liste_epee
        self.liste_bouclier = liste_bouclier
        self.liste_bottes = liste_bottes
        self.liste_soupe = liste_soupe
