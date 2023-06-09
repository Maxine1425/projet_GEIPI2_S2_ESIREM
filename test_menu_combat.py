import pygame
import time
import random
from Button import Button
from Battle import Battle
import os

def unes():
    time.sleep(1)



def Battle_Screen(opponent1, opponent2):

    pygame.init()
    combat = Battle(opponent1, opponent2)
    # Taille de la fenetre
    SCREEN_WIDTH = 990
    SCREEN_HEIGHT = 660

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Initialisation de Pygame
    pygame.init()

    # Creation de la fenetre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fond = pygame.image.load(
        "images/fond_menu.png").convert()  # on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
    screen.blit(fond, (0, 0))
    # Chargement des images

    fond_texte_combat = pygame.image.load("images/fond_texte_combat.png")
    floor1 = pygame.image.load("images/battlefloor.png")
    floor2 = pygame.image.load("images/battlefloor.png")
    salameche_image = pygame.image.load("images/Salameche.png")
    bulbizarre_image = pygame.image.load('images/Bulbizarre.png')
    hp_images = {
        'FULL': pygame.image.load('images/VIE_FULL.png'),
        'QC': pygame.image.load('images/VIEQC.png'),
        'TC': pygame.image.load('images/VIETC.png'),
        'DC': pygame.image.load('images/VIEDC.png'),
        'UC': pygame.image.load('images/VIEUC.png'),
        'EMPTY': pygame.image.load('images/VIE_EMPTY.png'),
    }
    bouton_attaque = pygame.image.load('images/attaque.png')
    bouton_soin = pygame.image.load('images/soin.png')

    # Variables globales
    battle_log = []

    # Creation des boutons
    attaque_button = Button(bouton_attaque, 800, SCREEN_HEIGHT - 140)
    soin_button = Button(bouton_soin, 815, SCREEN_HEIGHT - 80)
    # On check quel monstre est le plus rapide
    if opponent1.VIT > opponent2.VIT:
        fast_one = opponent1
        slow_one = opponent2
    elif opponent1.VIT == opponent2.VIT:
        a = random.randint(0, 1)
        if a == 0:
            fast_one = opponent1
            slow_one = opponent2
        else:
            fast_one = opponent2
            slow_one = opponent1
    else:
        fast_one = opponent2
        slow_one = opponent1

    fond_texte_combat = pygame.transform.scale_by(fond_texte_combat, 0.2)
    hp_images['FULL'] = pygame.transform.scale_by(hp_images['FULL'], 0.25)
    hp_images['QC'] = pygame.transform.scale_by(hp_images['QC'], 0.25)
    hp_images['TC'] = pygame.transform.scale_by(hp_images['TC'], 0.25)
    hp_images['DC'] = pygame.transform.scale_by(hp_images['DC'], 0.25)
    hp_images['UC'] = pygame.transform.scale_by(hp_images['UC'], 0.25)
    hp_images['EMPTY'] = pygame.transform.scale_by(hp_images['EMPTY'], 0.25)

    running = True
    while running:

        # Dessin des elements a l'ecran
        screen.blit(fond, (0, 0))

        # Dessin des monstres
        screen.blit(fond_texte_combat, (100, 520))
        screen.blit(floor1, (600, 150))
        screen.blit(floor2, (30, 250))
        screen.blit(bulbizarre_image, (620, 100))
        screen.blit(salameche_image, (50, 200))

        # Dessin des HP bar

        if opponent1.PV == opponent1.initial_max_PV:
            screen.blit(hp_images['FULL'], (70, 300))  # Salameche HP
        elif opponent1.PV < opponent1.initial_max_PV and opponent1.PV >= opponent1.initial_max_PV*(4/5):
            screen.blit(hp_images['QC'], (70, 300))
        elif opponent1.PV < opponent1.initial_max_PV*(4/5) and opponent1.PV >= opponent1.initial_max_PV * (3 / 5):
            screen.blit(hp_images['TC'], (70, 300))
        elif opponent1.PV < opponent1.initial_max_PV * (3 / 5) and opponent1.PV >= opponent1.initial_max_PV * (2 / 5):
            screen.blit(hp_images['DC'], (70, 300))
        elif opponent1.PV < opponent1.initial_max_PV * (2 / 5) and opponent1.PV >= opponent1.initial_max_PV * (1 / 5):
            screen.blit(hp_images['DC'], (70, 300))
        elif opponent1.PV < (1 / 5) and opponent1.PV > 0:
            screen.blit(hp_images['UC'], (70, 300))
        elif opponent1.PV == 0:
            screen.blit(hp_images['EMPTY'], (70, 300))


        if opponent2.PV == opponent2.initial_max_PV: #Bulbizarre HP
            screen.blit(hp_images['FULL'], (620, 200))
        elif opponent2.PV < opponent2.initial_max_PV and opponent2.PV >= opponent2.initial_max_PV * (4 / 5):
            screen.blit(hp_images['QC'], (620, 200))
        elif opponent2.PV < opponent2.initial_max_PV * (4 / 5) and opponent2.PV >= opponent2.initial_max_PV * (3 / 5):
            screen.blit(hp_images['TC'], (620, 200))
        elif opponent2.PV < opponent2.initial_max_PV * (3 / 5) and opponent2.PV >= opponent2.initial_max_PV * (2 / 5):
            screen.blit(hp_images['DC'], (620, 200))
        elif opponent2.PV < opponent2.initial_max_PV * (2 / 5) and opponent2.PV >= opponent2.initial_max_PV * (1 / 5):
            screen.blit(hp_images['DC'], (620, 200))
        elif opponent2.PV < (1 / 5) and opponent2.PV > 0:
            screen.blit(hp_images['UC'], (620, 200))
        elif opponent2.PV == 0:
            screen.blit(hp_images['EMPTY'], (620, 200))

        # Dessin des boutons
        attaque_button.draw(screen)
        soin_button.draw(screen)

        # Mise a jour de l'ecran
        pygame.display.flip()

        # Delai pour controler la vitesse du jeu
        unes()


        print("--------------------------------------------------")
        print(str(opponent1.name) + " a " + str(opponent1.PV) + "PV !")
        print(str(opponent2.name) + " a " + str(opponent2.PV) + "PV !")
        print("--------------------------------------------------")
        print(str(opponent1.name) + " a " + str(opponent1.VIT) + " de vitesse !")
        print(str(opponent2.name) + " a " + str(opponent2.VIT) + " de vitesse !")
        # Gestion des evenements
        for event in pygame.event.get():
            if opponent1.PV > 0 and opponent2.PV > 0:  # Check si un des deux combattants est KO
                if event.type == pygame.QUIT:
                    running = False
                    # Gestion des clics sur les boutons
                if attaque_button.is_clicked(event):
                    print("ATTAQUE")
                    if opponent2.PV <= 0.5 * opponent2.initial_max_PV:
                        choix2 = 2
                    else:
                        choix2 = 1

                    # Phase d'action

                    # On agit en fonction du monstre le plus rapide
                    if fast_one == opponent1:
                        unes()
                        print(opponent1.name + " attaque " + opponent2.name + "!")
                        fast_one.choix_attaque(1, slow_one)
                        # Avant que le second n'attaque, on check si il n'est pas mort
                        if slow_one.PV > 0:
                            unes()
                            if choix2 == 1:
                                print(slow_one.name + " attaque " + fast_one.name +  "!")
                            else:
                                print(slow_one.name + " se soigne !")

                            slow_one.choix_attaque(choix2, fast_one)
                        unes()


                    # Meme boucle que plus haut mais dans le cas ou c'est le second monstre le plus rapide
                    else:
                        if choix2 == 1:
                            unes()
                            print(opponent2.name + " attaque " + opponent1.name + "!")
                            fast_one.choix_attaque(choix2, slow_one)
                            if slow_one.PV > 0:
                                unes()
                                print(slow_one.name + " attaque !")
                                slow_one.choix_attaque(1, fast_one)
                    pass

                if soin_button.is_clicked(event):
                    print("SOIN")
                    if opponent2.PV <= 0.5 * opponent2.initial_max_PV:
                        choix2 = 2
                    else:
                        choix2 = 1

                    if fast_one == opponent1:
                        unes()
                        print(opponent1.name + " se soigne !")
                        fast_one.choix_attaque(2, slow_one)
                        unes()
                        slow_one.choix_attaque(choix2, fast_one)

                    else:
                        unes()
                        print(opponent2.name + " se soigne !")
                        fast_one.choix_attaque(2, slow_one)
                        unes()
                        slow_one.choix_attaque(choix2, fast_one)
                    pass

                    if opponent1.PV <= 0:
                        print(opponent1.name + " est KO!")
                        opponent1.ko_mon()
                    elif opponent2.PV <= 0:
                        print(opponent2.name + " est KO!")
                        opponent2.ko_mon()
                        break
                os.system('cls')
            else:
                if opponent1.PV <= 0:
                    print(opponent1.name + " est KO, le combat ne peut pas avoir lieu !\n")
                    unes()
                    break
                else:
                    print(opponent2.name + " est KO, le combat ne peut pas avoir lieu !\n")
                    unes()
                    break
