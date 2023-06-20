import random
import time

class LogiqueCombat:
    def __init__(self, joueur, monstre2):
        """
        Classe permettant de gerer toute la partie logique du combat.
        :param joueur: joueur prenant part au combat.
        :param monstre2: adversaire du joueur.
        """
        self.joueur = joueur
        self.en_cours = True
        self.combattant1 = joueur.liste_monstre[0]
        self.combattant2 = monstre2
        self.fast_one = self.comparaison_vitesse()
        self.slow_one = self.l_autre()

    def comparaison_vitesse(self):
        """
        Fonction permettant de trouver le monstre le plus rapide entre les deux.
        :return: Le monstre le plus rapide, si la vitesse est egale, un monstre au hasard.
        """
        if self.combattant1.VIT > self.combattant2.VIT:
            return self.combattant1
        elif self.combattant2.VIT > self.combattant1.VIT:
            return self.combattant2
        else:
            rand = [self.combattant1, self.combattant2]
        return random.choice(rand)

    def l_autre(self):
        """
        Deduit le monstre le plus lent a partir du resultat de comparaison_vitesse()
        :return: Le monstre le plus lent.
        """
        if self.fast_one == self.combattant1:
            return self.combattant2
        elif self.fast_one == self.combattant2:
            return self.combattant1

    def check_etat(self):
        """
        Check si les monstres sont KO ou pas.
        :return: 2 si le monstre 1 est KO, 1 si c'est l'autre. Retourne 0 si ils sont tout deux non KO.
        """
        if self.combattant1.PV <= 0:
            self.combattant1.ko_mon()
            return 2
        if self.combattant2.PV <= 0:
            self.combattant2.ko_mon()
            self.recompense()
            return 1
        return 0

    def tour(self, choix):
        """
        Fonction gerant le deroulement d'un tour.
        :param choix: choix du joueur, 1 si il attaque, 2 si il se soigne.
        """
        self.combattant1.choice = choix

        self.fast_one = self.comparaison_vitesse()
        self.slow_one = self.l_autre()

        # Si le plus rapide a choisi d'attaquer, on ecrit le texte necessaire.
        if self.fast_one.choice == 1:
            print(self.fast_one.nom + " attaque " + self.slow_one.nom + " !")
            self.fast_one.choix_attaque(self.slow_one)

            # On check si le monstre le plus lent est en vie apres l'attaque.
            if self.slow_one.PV > 0:
                if self.slow_one.choice == 1:
                    print(self.slow_one.nom + " attaque " + self.fast_one.nom + " !")
                    self.slow_one.choix_attaque(self.fast_one)

                elif self.slow_one.choice == 2:
                    print(self.slow_one.nom + " se soigne !")
                    self.slow_one.soin()

        # Si le monstre le plus rapide decide de se soigner.
        elif self.fast_one.choice == 2:
            print(self.fast_one.nom + " se soigne !")
            self.fast_one.soin()

            # Pas besoin de checker si le plus lent est KO comme le plus rapide n'a pas attaque.
            if self.slow_one.choice == 1:
                print(self.slow_one.nom + " attaque " + self.fast_one.nom + " !")
                self.slow_one.choix_attaque(self.fast_one)

            elif self.slow_one.choice == 2:
                print(self.slow_one.nom + " se soigne !")
                self.slow_one.soin()

    def choix_ordinateur(self):
        """
        Fonction permettant de determiner le choix de l'ordinateur.
        Il va toujours attaquer, sauf si il est en dessous de 50% de sa vie, dans ce cas la il va choisir aleatoirement
        entre se soigner et attquer.
        """
        if self.combattant2.PV < 0.5 * self.combattant2.initial_max_PV:
            self.combattant2.choice = random.randint(1,2)
        else:
            self.combattant2.choice = 1

    def calcul_soin(self, utilisateur):
        """
        Calcul les soins que l'utilisateur se fera si il choisit de se soigner.
        :param utilisateur: utlisateur du soin
        :return: Le soin potentiel.
        """
        if utilisateur.PV + (utilisateur.initial_max_PV * 0.5) <= utilisateur.initial_max_PV:
            return utilisateur.PV + (utilisateur.initial_max_PV * 0.5)
        elif utilisateur.PV + (utilisateur.initial_max_PV * 0.5) > utilisateur.initial_max_PV:
            return utilisateur.initial_max_PV - utilisateur.PV

    def calcul_degats(self, attaquant, cible):
        """
        Fonction permettant de calculer les degats potentiels d'un attaquant sur une cible.
        :param attaquant: attaquant
        :param cible: cible
        :return: les degats
        """
        raw_damage = attaquant.ATQ * 1.5
        adjusted_damage = raw_damage - (0.3 * cible.DEF)
        return max(adjusted_damage, 0)

    def recompense(self):
        """
        Fonction ajoutant de l'argent au joueur de facon aleatoire entre 250 et 1000
        """
        self.joueur.portefeuille.compteur += random.randint(250, 1000)
