import random
import time

from test_menu_combat import *
import Monstre
import Player
import Battle
from item import Item

joueur_test = Player.Player("Louis", 0, 1, 0, 0, 0)

joueur_test.print_monster_name()

salameche = Monstre.Monstre("Salameche", 10, "Attaque", "images/Salameche.png")
bulbizarre = Monstre.Monstre("Bulbizarre", 10, "Defense", "images/Bulbizarre.png")

joueur_test.add_monstre(salameche)

print(salameche.get_stats())
print(bulbizarre.get_stats())

epee = Item(1, "epee")
bouclier = Item(1, "bouclier")
soupe = Item(1, "soupe")
bottes = Item(1, "bottes")

joueur_test.ajouter_item(epee)
print(joueur_test.get_items())
joueur_test.ajouter_item(bouclier)
joueur_test.ajouter_item(soupe)
print(joueur_test.get_items())
joueur_test.ajouter_item(bottes)
print(joueur_test.get_items())

joueur_test.save_all()