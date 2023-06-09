import pygame
from pygame.locals import *
from datetime import datetime
from datetime import date
import Player

pygame.init()

class Menu:

    def __init__(self, joueur):
        self.joueur = joueur
        self.doit_lancer_menu = 1
        self.doit_lancer_combat = 0
    def menu(self, lance):

        if lance == 1:
            argent = self.joueur.wallet
            # Acceder a l'argent du joueur : argent.compteur
            # Acceder au mod du joueur : argent.mod
            # Ajouter un mod au joueur : argent.ajouter_mod(valeur)

            #creation de la fenetre principal
            fenetre = pygame.display.set_mode((990, 660),)

            #nom du jeu apparait
            pygame.display.set_caption("Jeux de Louis et Maxine")

            #affichage des fonds et boutton
            fond = pygame.image.load("images/fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
            fenetre.blit(fond, (0, 0)) #on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

            montant_x2 = 30
            montant_x5 = 100
            montant_x10 = 1000

            nombre_de_x2 = 0
            nombre_de_x5 = 0
            nombre_de_x10 = 0

            def afficher_menu_boutique(lance, fenetre):
                if lance == 1:
                    fenetre.blit(fond_menu_boutique, (350, 20))
                    fenetre.blit(mod_x2, (400, 70))
                    fenetre.blit(mod_x5,(500, 70))
                    fenetre.blit(mod_x10,(600, 70))
                    prix_x2 = font.render(str(montant_x2)+ " po", True, (0, 0, 0))
                    fenetre.blit(prix_x2, (415, 150))
                    prix_x5 = font.render(str(montant_x5)+ " po", True, (0, 0, 0))
                    fenetre.blit(prix_x5, (515, 150))
                    prix_x10 = font.render(str(montant_x10)+" po", True, (0, 0, 0))
                    fenetre.blit(prix_x10, (615, 150))

            def afficher_menu_monstre(lance, fenetre):
                if lance == 1:
                    fenetre.blit(fond_menu_boutique, (350, 20))
                    fenetre.blit(button_lancer_combat, (360,350))

            def afficher_menu_inventaire(lance, fenetre):
                if lance == 1:
                    fenetre.blit(fond_menu_boutique, (350,20))

                    nombre_x2 = font.render("vous avez : " + str(nombre_de_x2) , True, (0, 0, 0))
                    fenetre.blit(nombre_x2, (355,60))
                    fenetre.blit(mod_x2, (600,30))

                    nombre_x5 = font.render("vous avez : " + str(nombre_de_x5), True, (0, 0, 0))
                    fenetre.blit(nombre_x5, (355, 150))
                    fenetre.blit(mod_x5, (600, 120))

                    nombre_x10 = font.render("vous avez : " + str(nombre_de_x10), True, (0, 0, 0))
                    fenetre.blit(nombre_x10, (355, 240))
                    fenetre.blit(mod_x10, (600, 210))



            fond_donee = pygame.image.load("images/fond_donee.jpg").convert()
            # Creation de la surface de l'ombre
            ombre = pygame.Surface(fond_donee.get_size()).convert_alpha()
            ombre.fill((0, 0, 0, 70))  # Couleur de l'ombre (noir semi-transparent)

            # Position de l'ombre
            x_ombre = 0 + 5  # Decalage horizontal de l'ombre
            y_ombre = 0 + 5  # Decalage vertical de l'ombre

            # Affichage de l'ombre
            fenetre.blit(ombre, (x_ombre, y_ombre))
            fenetre.blit(fond_donee, (0, 0))

            button_boutique = pygame.image.load("images/button_boutique.png").convert_alpha() #l'image sera avec un fond transparant
            fenetre.blit(button_boutique, (30, 570))
            button_menu_monstre = pygame.image.load("images/button_menu-monstre.png").convert_alpha() #l'image sera avec un fond transparant
            fenetre.blit(button_menu_monstre, (220, 570))
            button_inventaire = pygame.image.load("images/button_inventaire.png").convert_alpha() #l'image sera avec un fond transparant
            fenetre.blit(button_inventaire, (460, 570))
            fond_menu_boutique = pygame.image.load("images/fond_boutique.jpg").convert()
            mod_x2 = pygame.image.load("images/X2.png").convert_alpha()
            mod_x5 = pygame.image.load("images/X5.png").convert_alpha()
            mod_x10 = pygame.image.load("images/X10.png").convert_alpha()
            button_lancer_combat = pygame.image.load("images/button_lancer_combat .png").convert_alpha()

            # creation des zones de click
            clickable_area_boutique = pygame.Rect((30, 570), (160, 49)) # (position)(taille)
            clickable_area_menu_monstre = pygame.Rect((220, 570), (210, 49))
            clickable_area_inventaire = pygame.Rect((460, 570), (168, 49))
            clickable_area_boutique_mod_2 = pygame.Rect((400, 70), (80, 80))
            clickable_area_boutique_mod_5 = pygame.Rect((500, 70), (80, 80))
            clickable_area_boutique_mod_10 = pygame.Rect((600, 70), (80, 80))
            clickable_area_lancer_combat = pygame.Rect((360,350),(200,48))

            #creation de l'orloge pour afficher l'heure
            horloge = pygame.time.Clock()

            pygame.display.flip() #ligne pour gerer le rafraichissement de la fenetre

            continuer = 1

            doit_lancer_menu_boutique = 0
            doit_lancer_menu_monstre = 0
            doit_lancer_menu_inventaire = 0

            #boucle de gestion de la fentre
            while continuer:
                for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
                    if event.type == QUIT:  # Si un de ces evenements est de type QUIT
                        continuer = 0  # On arrete la boucle
                        argent.stopper()
                    #boutique
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
                        if doit_lancer_menu_boutique == 0:
                            print("ouvre la boutique")
                            doit_lancer_menu_boutique = 1
                            doit_lancer_menu_monstre = 0
                            doit_lancer_menu_inventaire = 0
                            pygame.display.flip()
                        elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
                            doit_lancer_menu_boutique = 0
                            print("ferme la boutique")
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_2.collidepoint(
                            event.pos):
                        if self.joueur.check_argent(montant_x2):
                            print("x2")
                            self.joueur.achat(montant_x2)
                            argent.ajouter_mod(2)
                            nombre_de_x2 = nombre_de_x2 + 1

                        else:
                            print("pas assez d'argent ") #voir comment l'afficher
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_5.collidepoint(
                            event.pos):
                        if self.joueur.check_argent(montant_x5):
                            print("x5")
                            self.joueur.achat(montant_x5)
                            argent.ajouter_mod(5)
                            nombre_de_x5 = nombre_de_x5 + 1
                        else:
                            print("pas assez d'argent ") #voir comment l'afficher
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_10.collidepoint(
                            event.pos):
                        if self.joueur.check_argent(montant_x10):
                            print("x10")
                            self.joueur.achat(montant_x10)
                            argent.ajouter_mod(10)
                            nombre_de_x10 = nombre_de_x10 +1
                        else:
                            print("pas assez d'argent ") #voir comment l'afficher
                    #menu monstre
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
                        if doit_lancer_menu_monstre == 0:
                            print("ouvre menu monstre")
                            doit_lancer_menu_monstre= 1
                            doit_lancer_menu_boutique = 0
                            doit_lancer_menu_inventaire = 0
                            pygame.display.flip()
                        elif doit_lancer_menu_monstre == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
                            doit_lancer_menu_monstre = 0
                            print("ferme le menu monstre")
                    elif doit_lancer_menu_monstre == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_lancer_combat.collidepoint(event.pos):
                        print("lancer un combat")
                        self.doit_lancer_combat = 1
                        self.doit_lancer_menu = 0
                        continuer = 0
                        pygame.display.flip()
                    #menu inventaire
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
                        if doit_lancer_menu_inventaire == 0:
                            print("ouvre menu inventaire")
                            doit_lancer_menu_inventaire = 1
                            doit_lancer_menu_boutique = 0
                            doit_lancer_menu_monstre = 0
                            pygame.display.flip()
                        elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
                            doit_lancer_menu_inventaire = 0
                            print("ferme l inventaire")



                #permet de reactualiser le fond
                fenetre.blit(fond, (0, 0))
                fenetre.blit(ombre, (x_ombre, y_ombre))
                fenetre.blit(fond_donee, (0, 0))
                fenetre.blit(button_boutique, (30, 570))
                fenetre.blit(button_menu_monstre, (220, 570))
                fenetre.blit(button_inventaire, (460, 570))

                afficher_menu_boutique(doit_lancer_menu_boutique, fenetre)
                afficher_menu_monstre(doit_lancer_menu_monstre, fenetre)
                afficher_menu_inventaire(doit_lancer_menu_inventaire, fenetre)

                #afficher l'heure
                font = pygame.font.Font("Vogue.ttf", 20)  # Police principale
                heure = datetime.now()
                heure_1 = heure.strftime("%H:%M:%S")
                heure_a_afficher = font.render(heure_1, True, (0, 0, 0),)
                fenetre.blit(heure_a_afficher, (10, 40))

                #afficher la date
                font = pygame.font.Font("Vogue.ttf", 20)
                current_date = date.today()
                date_1 = current_date.strftime("%d/%m/%Y")
                date_a_afficher = font.render(date_1, True, (0, 0, 0))

                date_a_afficher_sans_fond = date_a_afficher.convert_alpha()
                fenetre.blit(date_a_afficher_sans_fond, (10, 10))


                #afficher l'argent
                font = pygame.font.Font("Vogue.ttf", 20)
                argent_a_afficher = font.render("Votre argent : " + str(argent.compteur) + " po", True, (0, 0, 0),)
                fenetre.blit(argent_a_afficher, (35, 100))

                #gere l'actualisation de l'heure
                pygame.display.flip()
                horloge.tick(60)


    def quitter(self):
        pygame.quit()