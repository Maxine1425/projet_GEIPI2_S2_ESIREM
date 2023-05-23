from threading import Thread
import time

class Afficher_heure(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        heure = time.strftime("%H:%M:%S", time.localtime())
        self.result = heure


    def result(self):
        return self.result