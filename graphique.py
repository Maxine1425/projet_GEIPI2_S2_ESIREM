import time

import pygame
import sys

from menu import Menu
import Player
from Battle import Battle
from test_menu_combat import Battle_Screen

import Monstre


# Creez les instances de Monster avec les parametres appropries
monstre_joueur = Monstre.Monstre("Monstre Joueur", 10, "Defense")
monstre_ordinateur = Monstre.Monstre("Monstre Ordinateur", 10, "Attaque")


# creation des objets
joueur = Player.Player("Louis", 50, 1, 0, 0, 0)
menu_principal = Menu(joueur)
combat = Battle(monstre_joueur, monstre_ordinateur)

lancer_menu = menu_principal.doit_lancer_menu
lancer_combat = menu_principal.doit_lancer_combat

while lancer_menu == 1:

    lancer_menu = menu_principal.doit_lancer_menu
    lancer_combat = menu_principal.doit_lancer_combat


    if lancer_menu == 1:
        menu_principal.menu(lancer_menu)
        menu_principal.doit_lancer_menu = 0

    elif lancer_combat == 1:
        Battle_Screen(monstre_joueur, monstre_ordinateur)
        menu_principal.quitter()
        menu_principal.doit_lancer_combat = 0



