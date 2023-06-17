import random
import pygame
from pygame.locals import *
from datetime import datetime
from datetime import date
import item
from menu_accueil import Menu_accueil


class Menu:

    def __init__(self, joueur):
        self.joueur = joueur
        self.doit_lancer_menu = 1
        self.doit_lancer_combat = 0
        self.temps_message = 0

    def quitter(self):
        pygame.quit()

    def menu(self, lance):
        pygame.init()
        menu = Menu_accueil()

        if lance == 1:

            argent = self.joueur.portefeuille

            # creation de la fenetre principal
            fenetre = pygame.display.set_mode((990, 660))

            # nom du jeu apparait
            pygame.display.set_caption("Jeux de Louis et Maxine")

            # initialisation des varriables
            doit_lancer_menu_boutique = 0
            doit_lancer_menu_monstre = 0
            doit_lancer_menu_inventaire = 0

            montant_x2 = 30
            montant_x5 = 100
            montant_x10 = 1000
            montant_epee = 1000
            montant_bouclier = 1000
            montant_bottes = 1000
            montant_soupe = 1000

            #nombre_de_x2 = 0
            #nombre_de_x5 = 0
            #nombre_de_x10 = 0

            nombre_epee = 0
            nombre_bouclier = 0
            nombre_bottes = 0
            nombre_soupe = 0


            epee = item.Item(1, "epee")
            epee.rare = 0
            epee.valeur_atq = 0
            bouclier = item.Item(1, "bouclier")
            bouclier.rare = 0
            bouclier.valeur_def = 0
            bottes = item.Item(1, "bottes")
            bottes.rare = 0
            bottes.valeur_vit = 0
            soupe = item.Item(1, "soupe")
            soupe.rare = 0
            soupe.valeur_pv = 0

            font = pygame.font.Font("Vogue.ttf", 20)

            #affichage de texte
            afficher_pas_assez_argent = False
            afficher_epee = False
            afficher_bouclier = False
            afficher_bottes = False
            afficher_soupe = False
            afficher_deja_un = False

            #chargement des images
            fond = pygame.image.load("images/fond_menu.png").convert()
            button_boutique = pygame.image.load("images/button_boutique.png").convert_alpha()  # l'image sera avec un fond transparant
            button_menu_monstre = pygame.image.load("images/button_menu-monstre.png").convert_alpha()  # l'image sera avec un fond transparant
            button_inventaire = pygame.image.load("images/button_inventaire.png").convert_alpha()  # l'image sera avec un fond transparant
            fond_menu_boutique = pygame.image.load("images/fond_boutique.jpg").convert()
            mod_x2 = pygame.image.load("images/X2.png").convert_alpha()
            mod_x5 = pygame.image.load("images/X5.png").convert_alpha()
            mod_x10 = pygame.image.load("images/X10.png").convert_alpha()
            epee_image = pygame.image.load("images/epee.png").convert_alpha()
            bouclier_image = pygame.image.load("images/bouclier.png").convert_alpha()
            bottes_image = pygame.image.load("images/bottes.png").convert_alpha()
            soupe_image = pygame.image.load("images/soupe.png").convert_alpha()
            button_lancer_combat = pygame.image.load("images/button_lancer_combat .png").convert_alpha()
            fond_donee = pygame.image.load("images/fond_donee.jpg").convert()
            button_vendre = pygame.image.load("images/button_vendre.png").convert_alpha()
            button_sauvergarde = pygame.image.load("images/button_sauvegarder.png").convert_alpha()
            button_charger = pygame.image.load("images/button_charger.png").convert_alpha()

            # creation des zones de click
            clickable_area_boutique = pygame.Rect((30, 570), (160, 49)) # (position)(taille)
            clickable_area_menu_monstre = pygame.Rect((220, 570), (210, 49))
            clickable_area_inventaire = pygame.Rect((460, 570), (168, 49))
            clickable_area_boutique_mod_2 = pygame.Rect((400, 70), (80, 80))
            clickable_area_boutique_mod_5 = pygame.Rect((500, 70), (80, 80))
            clickable_area_boutique_mod_10 = pygame.Rect((600, 70), (80, 80))
            clickable_area_boutique_item_epee = pygame.Rect((400, 170), (80, 80))
            clickable_area_boutique_item_bouclier = pygame.Rect((500, 170), (80, 80))
            clickable_area_boutique_item_bottes = pygame.Rect((600, 170), (80, 80))
            clickable_area_boutique_item_soupe = pygame.Rect((700, 170), (80, 80))
            clickable_area_lancer_combat = pygame.Rect((360, 350), (200, 48))
            clickable_area_vendre_epee = pygame.Rect((780, 150), (157, 49))
            clickable_area_vendre_bouclier = pygame.Rect((780, 220), (157, 49))
            clickable_area_vendre_bottes = pygame.Rect((780, 300), (157, 49))
            clickable_area_vendre_soupe = pygame.Rect((780, 370), (157, 49))
            clickable_area_charger = pygame.Rect((835, 570), (150, 49))
            clickable_area_sauvegarde = pygame.Rect((645,570), (187, 49))



            # affichage des fonds et boutton de la fenetre principal (le menu sans rien d'ouvert)
            fenetre.blit(fond, (0, 0))  # on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)
            fenetre.blit(button_boutique, (30, 570))
            fenetre.blit(button_menu_monstre, (220, 570))
            fenetre.blit(button_inventaire, (460, 570))
            # Creation de la surface de l'ombre
            ombre = pygame.Surface(fond_donee.get_size()).convert_alpha()
            ombre.fill((0, 0, 0, 70))  # Couleur de l'ombre (noir semi-transparent)

            # Position de l'ombre
            x_ombre = 0 + 5  # Decalage horizontal de l'ombre
            y_ombre = 0 + 5  # Decalage vertical de l'ombre

            # Affichage de l'ombre
            fenetre.blit(ombre, (x_ombre, y_ombre))
            fenetre.blit(fond_donee, (0, 0))

            #definition de la fonction afficher_menu_boutique
            def afficher_menu_boutique(lance, fenetre):
                if lance == 1:

                    fenetre.blit(fond_menu_boutique, (350, 20))
                    fenetre.blit(mod_x2, (400, 70))
                    fenetre.blit(mod_x5,(500, 70))
                    fenetre.blit(mod_x10,(600, 70))
                    fenetre.blit(epee_image, (400, 170))
                    fenetre.blit(bouclier_image, (500, 170))
                    fenetre.blit(bottes_image, (600, 170))
                    fenetre.blit(soupe_image, (700, 170))

                    prix_x2 = font.render(str(montant_x2) + " po", True, (0, 0, 0))
                    fenetre.blit(prix_x2, (415, 150))
                    prix_x5 = font.render(str(montant_x5)+ " po", True, (0, 0, 0))
                    fenetre.blit(prix_x5, (515, 150))
                    prix_x10 = font.render(str(montant_x10)+" po", True, (0, 0, 0))
                    fenetre.blit(prix_x10, (615, 150))
                    prix_epee = font.render(str(montant_epee)+" po", True, (0, 0, 0))
                    fenetre.blit(prix_epee, (415, 250))
                    prix_bouclier = font.render(str(montant_bouclier) + " po", True, (0, 0, 0))
                    fenetre.blit(prix_bouclier, (515, 250))
                    prix_bottes = font.render(str(montant_bottes) + " po", True, (0, 0, 0))
                    fenetre.blit(prix_bottes, (615, 250))
                    prix_soupe = font.render(str(montant_soupe) + " po", True, (0, 0, 0))
                    fenetre.blit(prix_soupe, (715, 250))
                    if afficher_pas_assez_argent:
                        pas_assez_argent = font.render("Pas assez d'argent !", True, (255, 255, 255))
                        fenetre.blit(pas_assez_argent, (400, 450))
                    if afficher_epee:
                        texte_epee = font.render("Vous avez achete une epee de rarete : " + str(epee.rare) + " et d'attaque : " + str(epee.valeur_atq),True, (255,255,255))
                        fenetre.blit(texte_epee, (50, 450))
                    if afficher_bouclier:
                        texte_bouclier = font.render("Vous avez achete un bouclier de rarete : " + str(bouclier.rare) + " et de defance : " + str(bouclier.valeur_def),True, (255,255,255))
                        fenetre.blit(texte_bouclier, (50, 450))
                    if afficher_bottes:
                        texte_bottes = font.render("Vous avez achete des bottes de rarete : " + str(bottes.rare) + " et de vitesse: " + str(bottes.valeur_vit),True, (255,255,255))
                        fenetre.blit(texte_bottes, (50, 450))
                    if afficher_soupe:
                        texte_soupe = font.render("Vous avez achete de la soupe de rarete : " + str(soupe.rare) + " et de PV : " + str(soupe.valeur_pv),True, (255,255,255))
                        fenetre.blit(texte_soupe, (50, 450))
                    if afficher_deja_un:
                        deja_un = font.render("Tu en as deja un !", True, (255, 255, 255))
                        fenetre.blit(deja_un, (400, 450))

            #definition de la fonction afficher_menu_monstre
            def afficher_menu_monstre(lance, fenetre):
                if lance == 1:
                    fenetre.blit(fond_menu_boutique, (350, 20))
                    fenetre.blit(button_lancer_combat, (360,350))

            #definition de la fonnction afficher_menu_inventaire
            def afficher_menu_inventaire(lance, fenetre):
                if lance == 1:
                    fenetre.blit(fond_menu_boutique, (350,20))

                    nombre_x2 = font.render(str(self.joueur.liste_mod[0]), True, (0, 0, 0))
                    fenetre.blit(nombre_x2, (355,60))
                    fenetre.blit(mod_x2, (400,30))

                    nombre_x5 = font.render(str(self.joueur.liste_mod[1]), True, (0, 0, 0))
                    fenetre.blit(nombre_x5, (500, 60))
                    fenetre.blit(mod_x5, (545, 30))

                    nombre_x10 = font.render(str(self.joueur.liste_mod[2]), True, (0, 0, 0))
                    fenetre.blit(nombre_x10, (645, 60))
                    fenetre.blit(mod_x10, (690, 30))

                    epee_inventaire = font.render("Rare : " + str(self.joueur.liste_epee.rare) + " et " + str(self.joueur.liste_epee.valeur_atq) + " d'attaque", True, (0, 0, 0))
                    fenetre.blit(epee_inventaire, (500,160))
                    fenetre.blit(epee_image, (380,130))
                    fenetre.blit(button_vendre,(780,150) )

                    bouclier_inventaire = font.render("Rare : " + str(self.joueur.liste_bouclier.rare) + " et " + str(self.joueur.liste_bouclier.valeur_def) + " de defense", True, (0, 0, 0))
                    fenetre.blit(bouclier_inventaire, (500,240))
                    fenetre.blit(bouclier_image, (380,210))
                    fenetre.blit(button_vendre, (780, 220))

                    bottes_inventaire = font.render("Rare : " + str(self.joueur.liste_bottes.rare) + " et " + str(self.joueur.liste_bottes.valeur_vit) + " de vitesse", True, (0, 0, 0))
                    fenetre.blit(bottes_inventaire, (500,320))
                    fenetre.blit(bottes_image, (380,290))
                    fenetre.blit(button_vendre, (780, 300))

                    soupe_inventaire = font.render("Rare : " + str(self.joueur.liste_soupe.rare) + " et " + str(self.joueur.liste_soupe.valeur_pv) + " de PV", True, (0, 0, 0))
                    fenetre.blit(soupe_inventaire, (500,390))
                    fenetre.blit(soupe_image, (380,350))
                    fenetre.blit(button_vendre, (780, 370))

            #creation de l'orloge pour afficher l'heure
            horloge = pygame.time.Clock()

            pygame.display.flip() #ligne pour gerer le rafraichissement de la fenetre

            continuer = 1

            #boucle de gestion de la fentre
            while continuer:
                for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
                    if event.type == QUIT:  # Si un de ces evenements est de type QUIT
                        continuer = 0  # On arrete la boucle
                        self.joueur.tout_sauvegarder()
                        argent.stopper()
                        pygame.quit()

                    #boutique
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if doit_lancer_menu_boutique == 0:
                            doit_lancer_menu_boutique = 1
                            doit_lancer_menu_monstre = 0
                            doit_lancer_menu_inventaire = 0

                        elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
                            doit_lancer_menu_boutique = 0

                    #achat mod_x2
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_2.collidepoint(
                            event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_x2):
                            self.joueur.achat(montant_x2)
                            argent.ajouter_mod(2)
                            #nombre_de_x2 = nombre_de_x2 + 1
                            self.joueur.liste_mod[0] += 1
                        else:
                            afficher_pas_assez_argent = True

                    #achat mod_x5
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_5.collidepoint(
                            event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_x5):
                            self.joueur.achat(montant_x5)
                            argent.ajouter_mod(5)
                            #nombre_de_x5 = nombre_de_x5 + 1
                            self.joueur.liste_mod[1] += 1
                        else:
                            afficher_pas_assez_argent = True

                    #achat mod_x10
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_10.collidepoint(
                            event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_x10):
                            self.joueur.achat(montant_x10)
                            argent.ajouter_mod(10)
                            #nombre_de_x10 = nombre_de_x10 +1
                            self.joueur.liste_mod[2] += 1
                        else:
                            afficher_pas_assez_argent = True

                    #achat epee
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_item_epee.collidepoint(event.pos) :
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_epee):
                            if self.joueur.ajouter_item(epee) == 1 :
                                afficher_epee = True
                                nombre_epee += 1
                                self.joueur.achat(montant_epee)
                                valeur_aleatoir_rare = random.randint(1, 5)
                                epee = item.Item(valeur_aleatoir_rare, "epee")
                                self.joueur.ajouter_item(epee)
                                print(nombre_epee)

                            elif self.joueur.ajouter_item(epee) == 2 :
                                afficher_deja_un = True
                        else:
                            afficher_pas_assez_argent = True

                    #achat bouclier
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_item_bouclier.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_bouclier):
                            if self.joueur.ajouter_item(bouclier) == 1 :
                                self.joueur.achat(montant_bouclier)
                                valeur_aleatoir_rare = random.randint(1, 5)
                                bouclier = item.Item(valeur_aleatoir_rare, "bouclier")
                                self.joueur.ajouter_item(bouclier)
                                afficher_bouclier = True
                                nombre_bouclier += 1
                            elif self.joueur.ajouter_item(bouclier) == 2 :
                                afficher_deja_un = True
                        else:
                            afficher_pas_assez_argent = True

                    #achat bottes
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_item_bottes.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_bottes):
                            if self.joueur.ajouter_item(bottes) == 1 :
                                self.joueur.achat(montant_bottes)
                                valeur_aleatoir_rare = random.randint(1, 5)
                                bottes = item.Item(valeur_aleatoir_rare, "bottes")
                                self.joueur.ajouter_item(bottes)
                                afficher_bottes = True
                                nombre_bottes += 1
                            elif self.joueur.ajouter_item(bottes) == 2 :
                                afficher_deja_un = True
                        else:
                            afficher_pas_assez_argent = True

                    #achat soupe
                    elif doit_lancer_menu_boutique == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_item_soupe.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        afficher_deja_un = False
                        if self.joueur.check_argent(montant_soupe):
                            if self.joueur.ajouter_item(soupe) == 1 :
                                self.joueur.achat(montant_soupe)
                                valeur_aleatoir_rare = random.randint(1, 5)
                                soupe = item.Item(valeur_aleatoir_rare, "soupe")
                                self.joueur.ajouter_item(soupe)
                                afficher_soupe = True
                                nombre_soupe += 1
                            elif self.joueur.ajouter_item(soupe) == 2 :
                                afficher_deja_un = True
                        else:
                            afficher_pas_assez_argent = True

                    #menu monstre
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        if doit_lancer_menu_monstre == 0:
                            doit_lancer_menu_monstre = 1
                            doit_lancer_menu_boutique = 0
                            doit_lancer_menu_inventaire = 0
                            pygame.display.flip()
                        elif doit_lancer_menu_monstre == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
                            doit_lancer_menu_monstre = 0
                    elif doit_lancer_menu_monstre == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_lancer_combat.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        self.doit_lancer_combat = 1
                        self.doit_lancer_menu = 0
                        continuer = 0
                        pygame.display.flip()

                    #menu inventaire
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
                        afficher_pas_assez_argent = False
                        afficher_epee = False
                        afficher_bouclier = False
                        afficher_bottes = False
                        afficher_soupe = False
                        if doit_lancer_menu_inventaire == 0:
                            doit_lancer_menu_inventaire = 1
                            doit_lancer_menu_boutique = 0
                            doit_lancer_menu_monstre = 0
                            pygame.display.flip()
                        elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
                            doit_lancer_menu_inventaire = 0

                    #vente epee
                    elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_vendre_epee.collidepoint(event.pos) and nombre_epee == 1:
                        print("epee vendu")
                        self.joueur.supprimer_item(epee)
                        self.joueur.vendre(montant_epee)
                        nombre_epee -= 1
                        print(nombre_epee)

                    #vente bouclier
                    elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_vendre_bouclier.collidepoint(event.pos) and nombre_bouclier == 1:
                        self.joueur.supprimer_item(bouclier)
                        self.joueur.vendre(montant_bouclier)
                        nombre_bouclier -= 1

                    #vente bottes
                    elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_vendre_bottes.collidepoint(event.pos) and nombre_bottes == 1:
                        self.joueur.supprimer_item(bottes)
                        self.joueur.vendre(montant_bottes)
                        nombre_bottes -= 1

                    #vente soupe
                    elif doit_lancer_menu_inventaire == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_vendre_soupe.collidepoint(event.pos) and nombre_soupe == 1:
                        self.joueur.supprimer_item(soupe)
                        self.joueur.vendre(montant_soupe)
                        nombre_soupe -= 1

                    #charger
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_charger.collidepoint(
                        event.pos):
                        self.joueur.charger_joueur(menu.retourner_pseudo())

                    #sauvergarder
                    elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_sauvegarde.collidepoint(
                        event.pos):
                        self.joueur.tout_sauvegarder()



                #permet de reactualiser le fond
                fenetre.blit(fond, (0, 0))
                fenetre.blit(ombre, (x_ombre, y_ombre))
                fenetre.blit(fond_donee, (0, 0))
                fenetre.blit(button_boutique, (30, 570))
                fenetre.blit(button_menu_monstre, (220, 570))
                fenetre.blit(button_inventaire, (460, 570))
                fenetre.blit(button_sauvergarde, (645,570))
                fenetre.blit(button_charger, (835, 570))

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
                argent_a_afficher = font.render("Votre argent : " + str(argent.compteur) + " po", True, (0, 0, 0))
                fenetre.blit(argent_a_afficher, (35, 100))

                #gere l'actualisation de l'heure
                pygame.display.flip()
                horloge.tick(60)

