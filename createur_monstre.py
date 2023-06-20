from monstre import *


class MonsterFactory:
    # Il faudra s'en servir pour optimiser le jeu
    @staticmethod
    def create_monster(monster_type, rare, chemin_image):
        if monster_type == 'attaque':
            return MonstreAttaque("Monstre Attaquant", 5, "chemin_image_attaque")
        elif monster_type == 'defense':
            return MonstreDefense("Monstre Defensif", 7, "chemin_image_defense")
