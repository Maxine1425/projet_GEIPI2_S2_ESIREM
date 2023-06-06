import random
import time
import unicodedata

class Battle:
    def __init__(self, monster1, monster2):
        """

        :param monster1: Ce monstre doit obligatoirement etre celui du joueur
        :param monster2: Ce monstre est celui de l'ordinateur
        """
        self.going_on = True
        self.opponent1 = monster1
        self.opponent2 = monster2

    def battle_speed_check(self): # Check qui est le monstre le plus rapide des deux
        if self.opponent1.VIT > self.opponent2.VIT:
            return self.opponent1
        elif self.opponent2.VIT > self.opponent1.VIT:
            return self.opponent2
        else:
            rand = [self.opponent1, self.opponent2]
        return random.choice(rand)

    def other_one(self): # Deduit le monstre le plus lent à partir du résultat de battle_speed_check()
        if self.battle_speed_check().name == self.opponent1.name:
            return self.opponent2
        elif self.battle_speed_check().name == self.opponent2.name:
            return self.opponent1

    def lets_battle(self):
        while self.opponent1.pv > 0 and self.opponent2.pv > 0: # Check si un des deux combattants est KO
            print(self.opponent1.name + " a " + str(self.opponent1.pv))
            print(self.opponent2.name + " a " + str(self.opponent2.pv))


            # Phase de choix

            # On demande au joueur de choisir une action, qui sera mise en attente jusqu'a la phase d'action
            # L'ordinateur choisit une action en fonction de ses PV actuels

            choix1 = int(input(self.opponent1.name + " c'est votre tour!\n\n1. Pour attaquer\n2. Pour se soigner\n"))
            if self.opponent2.pv <= 0.5 * self.opponent2.initial_max_pv:
                choix2 = 2
            else:
                choix2 = 1

            # Phase d'action

            # On check quel monstre est le plus rapide
            fast_one = self.battle_speed_check()
            slow_one = self.other_one()

            # On agit en fonction du monstre le plus rapide
            if fast_one == self.opponent1:
                if choix1 == 1:
                    time.sleep(1)
                    print(self.opponent1.name + " attaque " + self.opponent2.name + "!")
                    fast_one.choix_attaque(choix1, slow_one)
                    # Avant que le second n'attaque, on check si il n'est pas mort
                    if slow_one.pv > 0:
                        time.sleep(1)
                        slow_one.choix_attaque(choix2, fast_one)
                elif choix1 == 2:
                    time.sleep(1)
                    print(self.opponent1.name + " se soigne !")
                    fast_one.choix_attaque(choix1, slow_one)
                    time.sleep(1)
                    slow_one.choix_attaque(choix2, fast_one)


            # Meme boucle que plus haut mais dans le cas ou c'est le second monstre le plus rapide
            else:
                if choix2 == 1:
                    time.sleep(1)
                    print(self.opponent2.name + " attaque " + self.opponent1.name + "!")
                    fast_one.choix_attaque(choix2, slow_one)
                    if slow_one.pv > 0:
                        time.sleep(1)
                        slow_one.choix_attaque(choix1, fast_one)
                elif choix2 == 2:
                    time.sleep(1)
                    print(self.opponent2.name + " se soigne !")
                    fast_one.choix_attaque(choix2, slow_one)
                    time.sleep(1)
                    slow_one.choix_attaque(choix1, fast_one)


            # En fin de boucle, on check si un des deux monstre à en dessosu de 0 PV, et on le met KO si c'est le cas
            if self.opponent1.pv <= 0:
                print(f"{self.opponent1.name} est KO!")
                self.opponent1.ko_mon()
            elif self.opponent2.pv <= 0:
                print(f"{self.opponent2.name} est KO!")
                self.opponent2.ko_mon()
        self.going_on = False
