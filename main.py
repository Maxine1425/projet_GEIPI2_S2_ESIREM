import save_files

Pseudo = input("Veuillez rentrer votre pseudo :")

money = 7
mod = 5

mod = str(mod)
money = str(money)

player_data = money + "\n" + mod

save_files.sauvegarde_argent(Pseudo, player_data)
