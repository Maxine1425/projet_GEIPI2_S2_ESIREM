import save_files
import Monstre


Pseudo = input("Veuillez rentrer votre pseudo :")

money = 7
mod = 5

mod = str(mod)
money = str(money)

player_data = money + "\n" + mod

save_files.sauvegarde_argent(Pseudo, player_data)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque")

testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense")

a = testmnstr_attaque.show_stats()

print(a)

