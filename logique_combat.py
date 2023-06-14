import random


class LogiqueCombat:
    def __init__(self, monstre1, monstre2):
        """
        :param monstre1: Ce monstre doit obligatoirement etre celui du joueur
        :param monstre2: Ce monstre est celui de l'ordinateur
        """
        self.en_cours = True
        self.combattant1 = monstre1
        self.combattant2 = monstre2

    def comparaison_vitesse(self): # Check qui est le monstre le plus rapide des deux
        if self.combattant1.VIT > self.combattant2.VIT:
            return self.combattant1
        elif self.combattant2.VIT > self.combattant1.VIT:
            return self.combattant2
        else:
            rand = [self.combattant1, self.combattant2]
        return random.choice(rand)

    def l_autre(self): # Deduit le monstre le plus lent a partir du resultat de battle_speed_check()
        if self.comparaison_vitesse().name == self.combattant1.name:
            return self.combattant2
        elif self.comparaison_vitesse().name == self.combattant2.name:
            return self.combattant1
