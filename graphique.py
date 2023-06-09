from menu import Menu
import Player
import time

#cration des objet
joueur = Player.Player("Louis", 50, 1)
menu_principal = Menu(joueur)

#objet.atribue : lancer_menu prend la valeur de l'attribut "doit_lancer_menu" de l'objet "menu_principal"
lancer_menu = menu_principal.doit_lancer_menu

if lancer_menu == 1:
    menu_principal.menu(lancer_menu)
    print(lancer_menu)
elif lancer_menu == 0:
    print("lancer combat")









