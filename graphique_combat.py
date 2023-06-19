import pygame
import time
import random
from boutton import Button
from logique_combat import LogiqueCombat

pygame.init()

pygame.font.init()


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
    text = font.render("Le vainqueur est " + vainqueur.nom, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, rect.top - text_rect.height)  # Positionner au-dessus de l'image

    # Enregistrer le temps de début
    start_time = time.time()

    # Boucle pour afficher l'image pendant 2 secondes
    while time.time() - start_time < 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(fond, (0, 0))
        screen.blit(vainqueur_image, rect.topleft)
        screen.blit(text, text_rect.topleft)  # Affichage du texte
        pygame.display.flip()
        pygame.time.wait(50)  # Attendre un peu pour réduire l'utilisation du CPU



def ecran_combat(joueur, opponent2):
    opponent1 = joueur.liste_monstre[0]

    opponent1.PV = opponent1.initial_max_PV
    opponent2.PV = opponent2.initial_max_PV

    combat = LogiqueCombat(joueur, opponent2)
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
    opponent1_image = pygame.image.load(opponent1.chemin_image)
    opponent2_image = pygame.image.load(opponent2.chemin_image)
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

    opponent1_image = pygame.transform.scale_by(opponent1_image, 1.66)
    opponent2_image = pygame.transform.scale_by(opponent2_image, 1.66)

    hp_images['FULL'] = pygame.transform.scale_by(hp_images['FULL'], 0.25)
    hp_images['QC'] = pygame.transform.scale_by(hp_images['QC'], 0.25)
    hp_images['TC'] = pygame.transform.scale_by(hp_images['TC'], 0.25)
    hp_images['DC'] = pygame.transform.scale_by(hp_images['DC'], 0.25)
    hp_images['UC'] = pygame.transform.scale_by(hp_images['UC'], 0.25)
    hp_images['EMPTY'] = pygame.transform.scale_by(hp_images['EMPTY'], 0.25)

    running = True
    action_text = ""

    while running:
        screen.blit(fond, (0, 0))

        # Dessin des monstres
        screen.blit(floor1, (600, 150))
        screen.blit(floor2, (30, 250))
        screen.blit(opponent2_image, (620, 100))
        screen.blit(opponent1_image, (50, 200))

        # Dessin des HP bar

        if opponent1.PV == opponent1.initial_max_PV:
            screen.blit(hp_images['FULL'], (70, 200))  # Salameche HP
        elif opponent1.initial_max_PV > opponent1.PV >= opponent1.initial_max_PV * (4 / 5):
            screen.blit(hp_images['QC'], (70, 200))
        elif opponent1.initial_max_PV * (4 / 5) > opponent1.PV >= opponent1.initial_max_PV * (3 / 5):
            screen.blit(hp_images['TC'], (70, 200))
        elif opponent1.initial_max_PV * (3 / 5) > opponent1.PV >= opponent1.initial_max_PV * (2 / 5):
            screen.blit(hp_images['DC'], (70, 200))
        elif opponent1.initial_max_PV * (2 / 5) > opponent1.PV >= opponent1.initial_max_PV * (1 / 5):
            screen.blit(hp_images['DC'], (70, 200))
        elif opponent1.initial_max_PV * (1 / 5) > opponent1.PV > 0:
            screen.blit(hp_images['UC'], (70, 200))
        elif opponent1.PV == 0:
            screen.blit(hp_images['EMPTY'], (70, 200))

        if opponent2.PV == opponent2.initial_max_PV:  # Bulbizarre HP
            screen.blit(hp_images['FULL'], (620, 100))
        elif opponent2.initial_max_PV > opponent2.PV >= opponent2.initial_max_PV * (4 / 5):
            screen.blit(hp_images['QC'], (620, 100))
        elif opponent2.initial_max_PV * (4 / 5) > opponent2.PV >= opponent2.initial_max_PV * (3 / 5):
            screen.blit(hp_images['TC'], (620, 100))
        elif opponent2.initial_max_PV * (3 / 5) > opponent2.PV >= opponent2.initial_max_PV * (2 / 5):
            screen.blit(hp_images['DC'], (620, 100))
        elif opponent2.initial_max_PV * (2 / 5) > opponent2.PV >= opponent2.initial_max_PV * (1 / 5):
            screen.blit(hp_images['DC'], (620, 100))
        elif opponent2.initial_max_PV * (1 / 5) > opponent2.PV > 0:
            screen.blit(hp_images['UC'], (620, 100))
        elif opponent2.PV == 0:
            screen.blit(hp_images['EMPTY'], (620, 100))

        # Dessin des PV:
        pv1_text = f"{round(opponent1.PV)}/{opponent1.initial_max_PV} PV"
        pv2_text = f"{round(opponent2.PV)}/{opponent2.initial_max_PV} PV"

        # Dessin des boutons
        attaque_button.dessiner(screen)
        soin_button.dessiner(screen)

        afficher_texte(screen, pv1_text, text_font, WHITE, 70 + hp_images['FULL'].get_width() + 10, 300)
        afficher_texte(screen, pv2_text, text_font, WHITE, 620 + hp_images['FULL'].get_width() + 10, 200)

        pygame.display.flip()
        time.sleep(1)

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if attaque_button.est_clique(event):
                action_text = "ATTAQUE"
                combat.choix_ordinateur()
                combat.tour(1)


            if soin_button.est_clique(event):
                action_text = "SOIN"
                combat.choix_ordinateur()
                combat.tour(2)


            if combat.check_etat() == 1:
                ecran_victoire(opponent1)
                return
            elif combat.check_etat() == 2:
                ecran_victoire(opponent2)
                return

        afficher_texte(screen, action_text, text_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)
        pygame.display.flip()
        pygame.time.wait(50)