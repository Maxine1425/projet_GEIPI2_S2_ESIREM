import save_files
import Monstre
import Player

Pseudo = input("Veuillez rentrer votre pseudo :")

money = 8
mod = 5

mod = str(mod)
money = str(money)

player_data = money + "\n" + mod

save_files.sauvegarde_argent(Pseudo, player_data)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque")

testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense")

a = testmnstr_attaque.get_stats()
b = testmnstr_defense.get_stats()

monstre = [1, 2, 5, 7]

print(len(monstre))
print(a)
print(b)

test_joueur = Player.Player("Louis_Thin", money, mod)

test_joueur.add_monstre(testmnstr_attaque)

print(test_joueur.name,test_joueur.monster_list)
