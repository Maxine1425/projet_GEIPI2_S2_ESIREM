from menu import Menu
from logique_combat import LogiqueCombat
from graphique_combat import ecran_combat
from monstre import Monstre
from joueur import Joueur


# Creez les instances de Monster avec les parametres appropries
monstre_joueur = Monstre("Monstre Joueur", 10, "Attaque","images/Salameche.png")
monstre_ordinateur = Monstre("Monstre Ordinateur", 10, "Defense","images/Bulbizarre.png")


# creation des objets
joueur = Joueur("Louis", 0, 1, 0, 0, 0)
menu_principal = Menu(joueur)

joueur.ajouter_monstre(monstre_joueur)

while True :
    # recuperation des valeurs initiales
    lancer_menu = menu_principal.doit_lancer_menu
    lancer_combat = menu_principal.doit_lancer_combat

    if lancer_menu == 1:
        # appel de la methode menu()
        menu_principal.menu(lancer_menu)
        # mise a jour des valeurs apres l'appel de la methode
        print(lancer_menu)
    elif lancer_menu == 0:
        print("Lancer combat")
        ecran_combat(joueur, monstre_ordinateur)
        print("Combat termine")
        menu_principal.doit_lancer_menu = 1
