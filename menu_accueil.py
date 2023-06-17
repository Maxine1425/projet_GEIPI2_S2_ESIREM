import pygame
from pygame.locals import *


class Menu_accueil:

    def __init__(self):
        self.doit_lancer_menu_acceuil = 1
        self.doit_lancer_menu = 0
        self.pseudo = ""

    def menu_acceuil(self, lance):

        if lance == 1:

            pygame.init()
            fenetre = pygame.display.set_mode((990, 660))
            pygame.display.set_caption("fenetre d'acceuil")
            fond = pygame.image.load("images/fond_menu.png").convert()
            pygame.display.set_caption("Entree du pseudo")
            taille_police = 32
            police = pygame.font.Font(None, taille_police)
            self.pseudo = ""

            # Position et dimension du bouton
            bouton_rect = pygame.Rect((460, 590), (100, 40))

            continuer = True

            while continuer:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                    elif event.type == KEYDOWN:
                        if event.key == K_BACKSPACE:
                            self.pseudo = self.pseudo[:-1]

                        elif event.key == K_RETURN:
                            print(self.pseudo)
                            self.doit_lancer_menu_acceuil = 0
                            self.doit_lancer_menu = 1
                            continuer = False

                        else:
                            self.pseudo += event.unicode


                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1 and bouton_rect.collidepoint(event.pos):
                            print(self.pseudo)
                            self.doit_lancer_menu_acceuil = 0
                            self.doit_lancer_menu = 1

                            continuer = False


                fenetre.blit(fond, (0, 0))
                texte_surface = police.render(self.pseudo, True, (255, 255, 255))
                fenetre.blit(texte_surface, (330, 330))

                texte_label = police.render("Entrer votre nom d'utilisateur :", True, (255, 255, 255))
                fenetre.blit(texte_label, (330, 230))

                pygame.draw.rect(fenetre, (0, 255, 0), bouton_rect)
                bouton_texte = police.render("Valider", True, (255, 255, 255))
                fenetre.blit(bouton_texte, (bouton_rect.x + 10, bouton_rect.y + 10))

                pygame.display.flip()

            pygame.quit()




