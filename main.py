import random
import time

import Monstre
import Player
import Battle
from battle_screen import BattleScreen

joueur_test = Player.Player("Louis", 0, 1)

joueur_test.print_monster_name()

salameche = Monstre.Monstre("Salameche", 10, "Attaque")

bulbizarre = Monstre.Monstre("Bulbizarre", 10, "Defense")

joueur_test.add_monstre(salameche)

print(salameche.get_stats())
print(bulbizarre.get_stats())

ecran_combat = BattleScreen(salameche, bulbizarre)

ecran_combat.battle_screen()