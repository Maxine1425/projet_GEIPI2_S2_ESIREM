import random
import Monstre
import Player

player_name = input("Veuillez rentrer votre pseudo :")
monster_type = ["Attaque", "Defense"] #Differentes possibilites de type
monster_name = ["Ronflex", "Doduo", "Goelise", "Evoli", "Carapuce", "Metamorph"] #Differents noms possibles

money = 16
mod = 5
mod = str(mod)
money = str(money)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque") #Creation de Salameche, de rarete 10 et de type Attaque
testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense") #Creation de Bulbizarre, de rarete 10 et de type Defense

testmnstr1 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr2 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr3 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr4 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))
testmnstr5 = Monstre.Monstre(random.choice(monster_name), random.randint(1, 10), random.choice(monster_type))

testmnstr_end = Monstre.Monstre("Ronflex", random.randint(1, 10), "Defense") #Je fais celui la manuellement pour verifier que ca marche bien jusque la

a = testmnstr_attaque.get_stats()
b = testmnstr_defense.get_stats()
print(a)
print(b)

test_joueur = Player.Player(player_name, money, mod)

test_joueur.add_monstre(testmnstr_attaque) #Ajout des monstres a l'inventaire du joueur
test_joueur.add_monstre(testmnstr_defense)

test_joueur.add_monstre(testmnstr1)
test_joueur.add_monstre(testmnstr2)
test_joueur.add_monstre(testmnstr3)
test_joueur.add_monstre(testmnstr4)
test_joueur.add_monstre(testmnstr5)
test_joueur.add_monstre(testmnstr_end)

test_joueur.print_monster_name()

test_joueur.save_all() #Sauvegarde de l'argent dans un fichier txt et de l'inventaire de monstre dans un fichier txt
