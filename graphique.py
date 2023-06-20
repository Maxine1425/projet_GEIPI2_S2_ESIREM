from graphique_combat import ecran_combat
from joueur import Joueur
from menu import Menu
from menu_accueil import MenuAccueil
from monstre import Monstre


def lancer_jeu():
    menu_accueil = MenuAccueil()
    menu_accueil.menu_accueil(lance=1)
    print("pseudo = " + menu_accueil.pseudo) # Debug
    joueur = Joueur(menu_accueil.pseudo, 100000, 1, 0, 0, 0)
    menu_principal = Menu(joueur)

    while True:

        # recuperation des valeurs initiales
        lancer_menu = menu_principal.doit_lancer_menu
        lancer_menu_pour_la_1ere_fois = menu_accueil.doit_lancer_menu

        if lancer_menu == 1 and lancer_menu_pour_la_1ere_fois:

            # appel de la methode menu()
            menu_principal.menu(lancer_menu)

        elif lancer_menu == 0:
            # A chaque combat, on cr�e un nouveau monstre, pour �viter de combattre le meme � chaque fois.
            monstre_ordinateur = Monstre()

            # appel de la methode ecran_combat()
            ecran_combat(joueur, monstre_ordinateur)
            menu_principal.doit_lancer_menu = 1
