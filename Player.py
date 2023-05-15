from typing import List, Any

from Monstre import Monstre


class Player:
    monster_list: list[Monstre] = []

    def __init__(self, name, balance, mod):
        self.name = name
        self.balance = balance
        self.mod = mod

    def add_monstre(self, Monstre):
        inside_monster_list = self.monster_list
        length = len(inside_monster_list)
        try:
            if length == 0:
                inside_monster_list[0] = Monstre
            elif length != 0:
                inside_monster_list[length] = Monstre
        except:
            print("An error has occurred")

