import pygame
import time
import random
from Button import Button
from Battle import Battle
import os

pygame.init()

pygame.font.init()

def unes():
    time.sleep(1)

def afficher_texte(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def ecran_victoire(vainqueur):
    pygame.init()

    # Taille de la fenetre
    SCREEN_WIDTH = 990
    SCREEN_HEIGHT = 660

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Création de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fond = pygame.image.load("images/fond_menu.png").convert()
    screen.blit(fond, (0, 0))

    # Chargement de l'image du vainqueur
    vainqueur_image = pygame.image.load(vainqueur.chemin_image)
    rect = vainqueur_image.get_rect()
    rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Centrer l'image

    # Préparation du texte
    font = pygame.font.SysFont('Helvetica', 40)
    text = font.render("Le vainqueur est " + vainqueur.name, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, rect.top - text_rect.height)  # Positionner au-dessus de l'image

    # Enregistrer le temps de début
    start_time = time.time()

    # Boucle pour afficher l'image pendant 5 secondes
    while time.time() - start_time < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(fond, (0, 0))
        screen.blit(vainqueur_image, rect.topleft)
        screen.blit(text, text_rect.topleft)  # Affichage du texte
        pygame.display.flip()
        pygame.time.wait(50)  # Attendre un peu pour réduire l'utilisation du CPU


def ecran_combat(opponent1, opponent2):
    pygame.init()
    text_font = pygame.font.SysFont("Helvetica", 30)

    SCREEN_WIDTH, SCREEN_HEIGHT = 990, 660
    WHITE, BLACK = (255, 255, 255), (0, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fond = pygame.image.load("images/fond_menu.png").convert()
    screen.blit(fond, (0, 0))

    # Chargement des images
    floor1 = pygame.image.load("images/battlefloor.png")
    floor2 = pygame.image.load("images/battlefloor.png")
    salameche_image = pygame.image.load(opponent1.chemin_image)
    bulbizarre_image = pygame.image.load(opponent2.chemin_image)
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

    hp_images['FULL'] = pygame.transform.scale_by(hp_images['FULL'], 0.25)
    hp_images['QC'] = pygame.transform.scale_by(hp_images['QC'], 0.25)
    hp_images['TC'] = pygame.transform.scale_by(hp_images['TC'], 0.25)
    hp_images['DC'] = pygame.transform.scale_by(hp_images['DC'], 0.25)
    hp_images['UC'] = pygame.transform.scale_by(hp_images['UC'], 0.25)
    hp_images['EMPTY'] = pygame.transform.scale_by(hp_images['EMPTY'], 0.25)

    running = True
    clock = pygame.time.Clock()

    action_text = ""

    while running:
        screen.blit(fond, (0, 0))

        # Dessin des monstres
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
        elif opponent1.PV < opponent1.initial_max_PV * (1 / 5) and opponent1.PV > 0:
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
        elif opponent2.PV < opponent2.initial_max_PV * (1 / 5) and opponent2.PV > 0:
            screen.blit(hp_images['UC'], (620, 200))
        elif opponent2.PV == 0:
            screen.blit(hp_images['EMPTY'], (620, 200))

        # Dessin des PV:
        pv1_text = f"{round(opponent1.PV)}/{opponent1.initial_max_PV} PV"
        pv2_text = f"{round(opponent2.PV)}/{opponent2.initial_max_PV} PV"

        # Dessin des boutons
        attaque_button.draw(screen)
        soin_button.draw(screen)

        afficher_texte(screen, pv1_text, text_font, WHITE, 70 + hp_images['FULL'].get_width() + 10, 300)
        afficher_texte(screen, pv2_text, text_font, WHITE, 620 + hp_images['FULL'].get_width() + 10, 200)

        pygame.display.flip()
        unes()

        text_to_show = f"{opponent1.name} a {opponent1.PV}PV !\n{opponent2.name} a {opponent2.PV}PV !"
        combat_text_surface = text_font.render(text_to_show, True, BLACK)
        screen.blit(combat_text_surface, (220, 150))

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if attaque_button.is_clicked(event):
                action_text = "ATTAQUE"
                if opponent2.PV <= 0.5 * opponent2.initial_max_PV:
                    choix2 = random.randint(1,2)
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
                    action_text = "SOIN"
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
                    action_text = f"{opponent1.name} est KO!"
                    opponent1.ko_mon()
                    time.sleep(1)
                    running = False
                    ecran_victoire(opponent2)

                if opponent2.PV <= 0:
                    action_text = f"{opponent2.name} est KO!"
                    opponent2.ko_mon()
                    time.sleep(1)
                    running = False
                    ecran_victoire(opponent1)

            afficher_texte(screen, action_text, text_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()