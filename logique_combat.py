import random
import time

class LogiqueCombat:
    def __init__(self, joueur, monstre2):
        """
        :param monstre1: Ce monstre doit obligatoirement etre celui du joueur
        :param monstre2: Ce monstre est celui de l'ordinateur
        """
        self.joueur = joueur
        self.en_cours = True
        self.combattant1 = joueur.liste_monstre[0]
        self.combattant2 = monstre2
        self.fast_one = self.comparaison_vitesse()
        self.slow_one = self.l_autre()

    def comparaison_vitesse(self): # Check qui est le monstre le plus rapide des deux
        if self.combattant1.VIT > self.combattant2.VIT:
            return self.combattant1
        elif self.combattant2.VIT > self.combattant1.VIT:
            return self.combattant2
        else:
            rand = [self.combattant1, self.combattant2]
        return random.choice(rand)

    def l_autre(self): # Deduit le monstre le plus lent a partir du resultat de battle_speed_check()
        if self.fast_one == self.combattant1:
            return self.combattant2
        elif self.fast_one == self.combattant2:
            return self.combattant1

    def check_etat(self):
        if self.combattant1.PV <= 0:
            self.combattant1.ko_mon()

            return 2
        if self.combattant2.PV <= 0:
            self.combattant2.ko_mon()
            self.recompense()
            return 1
        return 0

    def tour(self, choix):
        self.combattant1.choice = choix

        self.fast_one = self.comparaison_vitesse()
        self.slow_one = self.l_autre()

        if self.fast_one.choice == 1:
            print(self.fast_one.nom + " attaque " + self.slow_one.nom + " !")
            self.fast_one.choix_attaque(self.slow_one)

            if self.slow_one.PV > 0:
                if self.slow_one.choice == 1:
                    print(self.slow_one.nom + " attaque " + self.fast_one.nom + " !")
                    self.slow_one.choix_attaque(self.fast_one)

                elif self.slow_one.choice == 2:
                    print(self.slow_one.nom + " se soigne !")
                    self.slow_one.soin()

        elif self.fast_one.choice == 2:
            print(self.fast_one.nom + " se soigne !")
            self.fast_one.soin()

            if self.slow_one.choice == 1:
                print(self.slow_one.nom + " attaque " + self.fast_one.nom + " !")
                self.slow_one.choix_attaque(self.fast_one)

            elif self.slow_one.choice == 2:
                print(self.slow_one.nom + " se soigne !")
                self.slow_one.soin()

    def choix_ordinateur(self):
        if self.combattant2.PV < 0.5 * self.combattant2.initial_max_PV:
            self.combattant2.choice = random.randint(1,2)
        else:
            self.combattant2.choice = 1

    def calcul_soin(self, utilisateur):
        if utilisateur.PV + (utilisateur.initial_max_PV * 0.5) <= utilisateur.initial_max_PV:
            return utilisateur.PV + (utilisateur.initial_max_PV * 0.5)
        elif utilisateur.PV + (utilisateur.initial_max_PV * 0.5) > utilisateur.initial_max_PV:
            return utilisateur.initial_max_PV - utilisateur.PV

    def calcul_degats(self, attaquant, cible):
        raw_damage = attaquant.ATQ * 1.5
        # Ajout de la réduction des dégâts basée sur la défense, comme dans la méthode 'deal_damage'
        adjusted_damage = raw_damage - (0.3 * cible.DEF)
        return max(adjusted_damage, 0)

    def recompense(self):
        self.joueur.portefeuille.compteur += random.randint(250,1000)
