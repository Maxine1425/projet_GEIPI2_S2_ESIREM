from threading import Thread
class Afficher_heure(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        datime = strftime("%H:%M:%S", time.localtime())
        self.result = datime
        time.sleep(0.2)

    def result(self):
        return self.result