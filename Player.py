from typing import List, Any
import json
from Monstre import Monstre


class Player:

    def __init__(self, name, balance, mod):
        self.name = name
        self.balance = balance
        self.mod = mod
        self.monster_list = []

    def add_monstre(self, Monstre):
        try:
            length = len(self.monster_list)
            if length == 0:
                self.monster_list.append(Monstre)
            else:
                self.monster_list.insert(length, Monstre)
        except:
            print("An error has occurred")

    def print_monster_name(self):
        length = len(self.monster_list)
        for i in range(length):
            print(self.monster_list[i].name)

    def sauvegarde_argent(self):
        file_name = self.name + "_money.txt"
        money_data = self.balance + "\n" + self.mod
        with open(file_name, 'w') as current:
            current.write(money_data)

    def sauvegarde_monstre(self):
        file_name = self.name + "_monster.txt"
        lenght = len(self.monster_list)
        with open(file_name, 'w') as current:
            for i in range(lenght):
                current.write(self.monster_list[i].name)
