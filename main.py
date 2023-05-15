import save_files
import Monstre
import Player

Pseudo = input("Veuillez rentrer votre pseudo :")

money = 16
mod = 5

mod = str(mod)
money = str(money)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque")

testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense")

a = testmnstr_attaque.get_stats()
b = testmnstr_defense.get_stats()

print(a)
print(b)

test_joueur = Player.Player("Louis_Thin", money, mod)

test_joueur.add_monstre(testmnstr_attaque)
test_joueur.add_monstre(testmnstr_defense)

print(test_joueur.name)

test_joueur.print_monster_name()

test_joueur.sauvegarde_argent()

test_joueur.sauvegarde_monstre()