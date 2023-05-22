import os
import random
import Monstre
import Player
import time


# player_name = input("Veuillez rentrer votre pseudo :")
#
# money = 16
# mod = 5
# mod = str(mod)
# money = str(money)
#
# testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque") #Creation de Salameche, de rarete 10 et de type Attaque
# testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense") #Creation de Bulbizarre, de rarete 10 et de type Defense
#
#
# test_joueur = Player.Player(player_name, money, mod)
#
# test_joueur.add_monstre(testmnstr_attaque) #Ajout des monstres a l'inventaire du joueur
# test_joueur.add_monstre(testmnstr_defense)
#
# BattleGoesOn = True
#
# while BattleGoesOn:
#     print(str(testmnstr_attaque.name) + " a " + str(testmnstr_attaque.PV) + " PV")
#     print(str(testmnstr_defense.name) + " a " + str(testmnstr_defense.PV) + " PV")
#
#     choice = input("\n" + str(testmnstr_attaque.name) + " choisit une action...\n1 Pour attaquer.\n2 Pour se soigner.\n...   ")
#     choice = int(choice)
#     testmnstr_attaque.choix_attaque(choice, testmnstr_defense)
#     validChoice = False
#     while validChoice == False:
#         if choice == 1:
#             prompt = testmnstr_attaque.name + " attaque " + testmnstr_defense.name + "!\n"
#             validChoice = True
#         elif choice == 2:
#             prompt = testmnstr_attaque.name + " s'est soigne !\n"
#             validChoice = True
#         else:
#             prompt = "Selectionnez un choix valide !\n"
#
#     for char in prompt:
#         print(char, end='')
#         time.sleep(.025)
#
#     if int(testmnstr_defense.PV) == 0:
#         loser = str(testmnstr_defense.name)
#         winner = str(testmnstr_attaque.name)
#         testmnstr_defense.koMon()
#         BattleGoesOn = False
#         break
#
#     print(str(testmnstr_attaque.name) + " a " + str(testmnstr_attaque.PV) + " PV")
#     print(str(testmnstr_defense.name) + " a " + str(testmnstr_defense.PV) + " PV")
#
#     choice = input("\n" + str(testmnstr_defense.name) + " choisit une action...\n1 Pour attaquer.\n2 Pour se soigner.\n...   ")
#     choice = int(choice)
#     testmnstr_defense.choix_attaque(choice, testmnstr_attaque)
#
#     validChoice = False
#     while validChoice == False:
#         if choice == 1:
#             prompt = testmnstr_defense.name + " attaque " + testmnstr_attaque.name + "!\n"
#             validChoice = True
#         elif choice == 2:
#             prompt = testmnstr_defense.name + " s'est soigne !\n"
#             validChoice = True
#         else:
#             prompt = "Selectionnez un choix valide !\n"
#
#     for char in prompt:
#         print(char, end='')
#         time.sleep(.025)
#
#     if int(testmnstr_attaque.PV) == 0:
#         loser = str(testmnstr_attaque.name)
#         winner = str(testmnstr_defense.name)
#         testmnstr_attaque.koMon()
#         BattleGoesOn = False
#         break
#
# print(loser + " a 0 PV!\n")
# time.sleep(0.8)
# print(loser + " ne peux plus se battre!\n")
# time.sleep(0.8)
# print(winner + " a gagne !")
# time.sleep(0.8)

class Battle:
    def __init__(self, Monster1, Monster2):
        self.goingOn = True
        self.opponent1 = Monster1
        self.opponent2 = Monster2

    def battleSpeedCheck(self):
        if self.opponent1.VIT > self.opponent2.VIT:
            return self.opponent1
        elif self.opponent2.VIT > self.opponent1.VIT:
            return self.opponent2
        else:
            rand = [self.opponent1, self.opponent2]
        return random.choice(rand)

    def otherOne(self):
        fastest = self.battleSpeedCheck()
        if fastest.name == self.opponent1.name:
            return self.opponent2
        elif fastest.name == self.opponent2.name:
            return self.opponent1

    def letsBattle(self):
        fast_one = self.battleSpeedCheck()
        slow_one = self.otherOne()
        print(fast_one.name + " has " + str(fast_one.VIT) + " SPD\n")
        print(slow_one.name + " has " + str(slow_one.VIT) + " SPD\n")

        while self.goingOn:
            




