import random


class Item :
    def __init__(self,rare,type):
        if type == "epee" :
            if rare == 1 :
                self.valeur_atq = random.randint(1, 50)
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 2 :
                self.valeur_atq = random.randint(50, 100)
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 3 :
                self.valeur_atq = random.randint(100, 150)
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 4 :
                self.valeur_atq = random.randint(150, 200)
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 5 :
                self.valeur_atq = random.randint(200, 150)
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = 0
        if type == "soupe":
            if rare == 1:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = random.randint(1, 50)
                self.valeur_vit = 0
            if rare == 2:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = random.randint(50, 100)
                self.valeur_vit = 0
            if rare == 3:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = random.randint(100, 150)
                self.valeur_vit = 0
            if rare == 4:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = random.randint(150, 200)
                self.valeur_vit = 0
            if rare == 5:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = random.randint(200, 150)
                self.valeur_vit = 0
        if type == "bottes":
            if rare == 1:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = random.randint(1, 50)
            if rare == 2:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = random.randint(50, 100)
            if rare == 3:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = random.randint(100, 150)
            if rare == 4:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = random.randint(150, 200)
            if rare == 5:
                self.valeur_atq = 0
                self.valeur_def = 0
                self.valeur_pv = 0
                self.valeur_vit = random.randint(200, 150)
        if type == "bouclier":
            if rare == 1:
                self.valeur_atq = 0
                self.valeur_def = random.randint(1, 50)
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 2:
                self.valeur_atq = 0
                self.valeur_def = random.randint(50, 100)
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 3:
                self.valeur_atq = 0
                self.valeur_def = random.randint(100, 150)
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 4:
                self.valeur_atq = 0
                self.valeur_def = random.randint(150, 200)
                self.valeur_pv = 0
                self.valeur_vit = 0
            if rare == 5:
                self.valeur_atq = 0
                self.valeur_def = random.randint(200, 150)
                self.valeur_pv = 0
                self.valeur_vit = 0