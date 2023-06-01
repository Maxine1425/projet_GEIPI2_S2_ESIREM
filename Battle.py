import os
import random
import pygame
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
        """

        :param Monster1: Ce monstre doit obligatoirement etre celui du joueur
        :param Monster2: Ce monstre est celui de l'ordinateur
        """
        self.going_on = True
        self.opponent1 = Monster1
        self.opponent2 = Monster2

    def battle_speed_check(self):
        if self.opponent1.VIT > self.opponent2.VIT:
            return self.opponent1
        elif self.opponent2.VIT > self.opponent1.VIT:
            return self.opponent2
        else:
            rand = [self.opponent1, self.opponent2]
        return random.choice(rand)

    def other_one(self, fastest):
        if fastest.name == self.opponent1.name:
            return self.opponent2
        elif fastest.name == self.opponent2.name:
            return self.opponent1
    def lets_battle(self):
        while self.opponent1.PV > 0 and self.opponent2.PV > 0:
            print(self.opponent1.name + " a " + str(self.opponent1.PV))
            print(self.opponent2.name + " a " + str(self.opponent2.PV))
            # Phase de choix
            choix1 = int(input(self.opponent1.name + " c'est votre tour!\n\n1. Pour attaquer\n2. Pour se soigner\n"))
            if self.opponent2.PV <= 0.5 * self.opponent2.initial_max_PV:
                choix2 = 2
            else:
                choix2 = 1

            # Phase d'action
            fast_one = self.battle_speed_check()
            slow_one = self.other_one(fast_one)

            if fast_one == self.opponent1:
                if choix1 == 1:
                    time.sleep(1)
                    print(self.opponent1.name + " attaque " + self.opponent2.name + "!")
                    fast_one.choix_attaque(choix1, slow_one)
                    if slow_one.PV > 0:
                        time.sleep(1)
                        slow_one.choix_attaque(choix2, fast_one)
                elif choix1 == 2:
                    time.sleep(1)
                    print(self.opponent1.name + " se soigne !")
                    fast_one.choix_attaque(choix1, slow_one)
                    time.sleep(1)
                    slow_one.choix_attaque(choix2, fast_one)


            else:
                if choix2 == 1:
                    time.sleep(1)
                    print(self.opponent2.name + " attaque " + self.opponent1.name + "!")
                    fast_one.choix_attaque(choix2, slow_one)
                    if slow_one.PV > 0:
                        time.sleep(1)
                        slow_one.choix_attaque(choix1, fast_one)
                elif choix2 == 2:
                    time.sleep(1)
                    print(self.opponent2.name + " se soigne !")
                    fast_one.choix_attaque(choix2, slow_one)
                    time.sleep(1)
                    slow_one.choix_attaque(choix1, fast_one)

            if self.opponent1.PV <= 0:
                print(f"{self.opponent1.name} est KO!")
                self.opponent1.koMon()
            elif self.opponent2.PV <= 0:
                print(f"{self.opponent2.name} est KO!")
                self.opponent2.koMon()
        self.goingOn = False
