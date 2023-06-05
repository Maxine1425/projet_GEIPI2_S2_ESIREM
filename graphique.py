from menu import Menu
import Player
import time

joueur = Player.Player("Louis", 50, 1)

menu_principal = Menu(joueur)
menu_principal.menu()