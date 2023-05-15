import random
import Monstre
import Player

monster_type = ["Attaque", "Defense"]
monster_name = ["Ronflex", "Doduo", "Goelise", "Evoli", "Carapuce", "Metamorph"]

money = 16
mod = 5
mod = str(mod)
money = str(money)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, random.choice(monster_type))
testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense")

testmnstr1 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr2 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr3 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr4 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr5 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))

testmnstr_end = Monstre.Monstre("Ronflex", random.randint(1, 10), "Defense")

a = testmnstr_attaque.get_stats()
b = testmnstr_defense.get_stats()

print(a)
print(b)

test_joueur = Player.Player("Louis_Thin", money, mod)

test_joueur.add_monstre(testmnstr_attaque)
test_joueur.add_monstre(testmnstr_defense)

test_joueur.add_monstre(testmnstr1)
test_joueur.add_monstre(testmnstr2)
test_joueur.add_monstre(testmnstr3)
test_joueur.add_monstre(testmnstr4)
test_joueur.add_monstre(testmnstr5)
test_joueur.add_monstre(testmnstr_end)

test_joueur.print_monster_name()

test_joueur.sauvegarde_argent()
test_joueur.sauvegarde_monstre()