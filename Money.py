import threading
import time

class Compteur:
    def __init__(self):
        self.compteur = 0
        self.arret = False

    def incrementer(self):
        while not self.arret:
            self.compteur += 1
            time.sleep(1)  # Pause d'une seconde

    def soustraire(self, montant):
        if self.compteur-montant >= 0:
            self.compteur -= montant
            return True
        else:
            return False

    def demarrer(self):
        self.thread = threading.Thread(target=self.incrementer)
        self.thread.start()  # Lancement du thread

    def stopper(self):
        self.arret = True
        self.thread.join()  # Attente de la fin du thread
