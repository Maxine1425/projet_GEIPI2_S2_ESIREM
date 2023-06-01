import random
import time

import Monstre
import Player
import Battle

joueur_test = Player.Player("Louis", 0, 1)

joueur_test.print_monster_name()

salameche = Monstre.Monstre("Salameche", 10, "Attaque")

bulbizarre = Monstre.Monstre("Bulbizarre", 10, "Defense")

joueur_test.add_monstre(salameche)

print(salameche.get_stats())
print(bulbizarre.get_stats())

combat = Battle.Battle(salameche,bulbizarre)

combat.lets_battle()