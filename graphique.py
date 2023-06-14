import time

import pygame

from menu import Menu
import Player
from Battle import Battle
from test_menu_combat import ecran_combat

import Monstre


# Creez les instances de Monster avec les parametres appropries
monstre_joueur = Monstre.Monstre("Monstre Joueur", 10, "Defense", "images/Salameche.png")
monstre_ordinateur = Monstre.Monstre("Monstre Ordinateur", 10, "Attaque", "images/Bulbizarre.png")


# creation des objets
joueur = Player.Player("Louis", 50, 1, 0, 0, 0)
joueur.add_monstre(monstre_joueur)
menu_principal = Menu(joueur)
combat = Battle(monstre_joueur, monstre_ordinateur)


while True :
    # recuperation des valeurs initiales
    lancer_menu = menu_principal.doit_lancer_menu
    lancer_combat = menu_principal.doit_lancer_combat

    if lancer_menu == 1:
        # appel de la methode menu()
        menu_principal.menu(lancer_menu)
        # mise a jour des valeurs apres l'appel de la methode
        print(lancer_menu)
    elif lancer_menu == 0:
        print("Lancer combat")
        ecran_combat(monstre_joueur, monstre_ordinateur)
        print("Combat termine")
        menu_principal.doit_lancer_menu = 1







