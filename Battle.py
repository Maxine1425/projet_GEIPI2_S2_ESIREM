import random
import Monstre
import Player
import time

player_name = input("Veuillez rentrer votre pseudo :")

money = 16
mod = 5
mod = str(mod)
money = str(money)

testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque") #Creation de Salameche, de rarete 10 et de type Attaque
testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense") #Creation de Bulbizarre, de rarete 10 et de type Defense


test_joueur = Player.Player(player_name, money, mod)

test_joueur.add_monstre(testmnstr_attaque) #Ajout des monstres a l'inventaire du joueur
test_joueur.add_monstre(testmnstr_defense)

BattleGoesOn = True

while BattleGoesOn:
    print(str(testmnstr_attaque.name) + " a " + str(testmnstr_attaque.PV) + " PV")
    print(str(testmnstr_defense.name) + " a " + str(testmnstr_defense.PV) + " PV")

    choice = input("\n" + str(testmnstr_attaque.name) + " choisit une action...")
    choice = int(choice)
    testmnstr_attaque.choix_attaque(choice, testmnstr_defense)
    validChoice = False
    while validChoice == False:
        if choice == 1:
            prompt = testmnstr_attaque.name + " attaque " + testmnstr_defense.name + "!\n"
            validChoice = True
        elif choice == 2:
            prompt = testmnstr_attaque.name + " s'est soigne !\n"
            validChoice = True
        else:
            prompt = "Selectionnez un choix valide !\n"

    for char in prompt:
        print(char, end='')
        time.sleep(.025)

    if int(testmnstr_defense.PV) == 0:
        loser = str(testmnstr_defense.name)
        winner = str(testmnstr_attaque.name)
        BattleGoesOn = False
        break

    print(str(testmnstr_attaque.name) + " a " + str(testmnstr_attaque.PV) + " PV")
    print(str(testmnstr_defense.name) + " a " + str(testmnstr_defense.PV) + " PV")

    choice = input("\n" + str(testmnstr_defense.name) + " choisit une action...")
    choice = int(choice)
    testmnstr_defense.choix_attaque(choice, testmnstr_attaque)

    validChoice = False
    while validChoice == False:
        if choice == 1:
            prompt = testmnstr_defense.name + " attaque " + testmnstr_attaque.name + "!\n"
            validChoice = True
        elif choice == 2:
            prompt = testmnstr_defense.name + " s'est soigne !\n"
            validChoice = True
        else:
            prompt = "Selectionnez un choix valide !\n"

    for char in prompt:
        print(char, end='')
        time.sleep(.025)

    if int(testmnstr_attaque.PV) == 0:
        loser = str(testmnstr_attaque.name)
        winner = str(testmnstr_defense.name)
        BattleGoesOn = False
        break

print(loser + " a 0 PV!\n")
time.sleep(0.8)
print(loser + " ne peux plus se battre!\n")
time.sleep(0.8)
print(winner + " a gagne !")
