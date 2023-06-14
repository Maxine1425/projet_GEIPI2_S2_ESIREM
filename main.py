import random
import time

from test_menu_combat import *
import Monstre
import Player
import Battle
from battle_screen import BattleScreen

joueur_test = Player.Player("Louis", 0, 1, 0, 0, 0)

joueur_test.print_monster_name()

salameche = Monstre.Monstre("Salameche", 10, "Attaque", "images/Salameche.png")

bulbizarre = Monstre.Monstre("Bulbizarre", 10, "Defense", "images/Bulbizarre.png")

joueur_test.add_monstre(salameche)

print(salameche.get_stats())
print(bulbizarre.get_stats())

ecran_combat(salameche, bulbizarre)