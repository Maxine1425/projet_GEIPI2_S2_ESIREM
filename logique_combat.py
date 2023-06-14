import random
import time

class LogiqueCombat:
    def __init__(self, joueur, monstre2):
        """
        :param monstre1: Ce monstre doit obligatoirement etre celui du joueur
        :param monstre2: Ce monstre est celui de l'ordinateur
        """
        self.en_cours = True
        self.combattant1 = joueur.liste_monstre[0]
        self.combattant2 = monstre2
        self.fast_one = self.comparaison_vitesse()
        self.slow_one = self.l_autre()
        self.choix1 = 1
        self.choix2 = 1

    def comparaison_vitesse(self): # Check qui est le monstre le plus rapide des deux
        if self.combattant1.VIT > self.combattant2.VIT:
            return self.combattant1
        elif self.combattant2.VIT > self.combattant1.VIT:
            return self.combattant2
        else:
            rand = [self.combattant1, self.combattant2]
        return random.choice(rand)

    def l_autre(self): # Deduit le monstre le plus lent a partir du resultat de battle_speed_check()
        if self.comparaison_vitesse().nom == self.combattant1.nom:
            return self.combattant2
        elif self.comparaison_vitesse().nom == self.combattant2.nom:
            return self.combattant1

    def check_etat(self):
        if self.combattant1.PV <= 0:
            self.combattant1.ko_mon()
            return 2
        if self.combattant2.PV <= 0:
            self.combattant2.ko_mon()
            return 1
        return 0


    def soin(self):
        if self.fast_one == self.combattant1:
            time.sleep(1)
            print(self.combattant1.nom + " se soigne !")
            self.fast_one.choix_attaque(2, self.slow_one)
            time.sleep(1)
            self.slow_one.choix_attaque(self.choix2, self.fast_one)

        else:
            time.sleep(1)
            print(self.combattant2.nom + " se soigne !")
            self.fast_one.choix_attaque(2, self.slow_one)
            time.sleep(1)
            self.slow_one.choix_attaque(self.choix2, self.fast_one)
        pass

    def choix_ordinateur(self):
        if self.combattant2.PV <= 0.5 * self.combattant2.initial_max_PV:
            self.choix2 = random.randint(1, 2)
        else:
            self.choix2 = 1

    def phase_action(self):
        if self.fast_one == self.combattant1:
            time.sleep(1)
            print(self.combattant1.nom + " attaque " + self.combattant2.nom + "!")
            self.fast_one.choix_attaque(1, self.slow_one)
            # Avant que le second n'attaque, on check si il n'est pas mort
            if self.slow_one.PV > 0:
                time.sleep(1)
                if self.choix2 == 1:
                    print(self.slow_one.nom + " attaque " + self.fast_one.nom + "!")
                else:
                    print(self.slow_one.nom + " se soigne !")
            self.slow_one.choix_attaque(self.choix2, self.fast_one)
            time.sleep(1)
        # Meme boucle que plus haut mais dans le cas ou c'est le second monstre le plus rapide
        else:
            if self.choix2 == 1:
                time.sleep(1)
                print(self.combattant2.nom + " attaque " + self.combattant1.nom + "!")
                self.fast_one.choix_attaque(self.choix2, self.slow_one)
                if self.slow_one.PV > 0:
                    time.sleep(1)
                    print(self.slow_one.nom + " attaque !")
                    self.slow_one.choix_attaque(1, self.fast_one)
        pass