import pygame
from pygame.locals import *
from datetime import datetime
from datetime import date
from Money import Compteur
pygame.init()

#creation d'un compteur pour afficher argent
argent = Compteur()
argent.demarrer()

#creation de la fenetre principal
fenetre = pygame.display.set_mode((990, 660),)

#nom du jeu apparait
pygame.display.set_caption("Jeux")

#affichage des fonds et boutton
fond = pygame.image.load("images/fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
fenetre.blit(fond, (0, 0)) #on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

def afficher_menu(test, fenetre):
    if test == 1:
        fenetre.blit(fond_menu_boutique, (350, 20))
        fenetre.blit(mod_x2, (400, 70))
        fenetre.blit(mod_x5,(500, 70))
        fenetre.blit(mod_x10,(600, 70))



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

# creation des zones de click
clickable_area_boutique = pygame.Rect((30, 570), (160, 49)) # (position)(taille)
clickable_area_menu_monstre = pygame.Rect((220, 570), (210, 49))
clickable_area_inventaire = pygame.Rect((460, 570), (168, 49))
clickable_area_boutique_mod_2 = pygame.Rect((400, 70), (80, 80))
clickable_area_boutique_mod_5 = pygame.Rect((500, 70), (80, 80))
clickable_area_boutique_mod_10 = pygame.Rect((600, 70), (80, 80))

#creation de l'orloge pour afficher l'heure
horloge = pygame.time.Clock()

pygame.display.flip() #ligne pour gerer le rafraichissement de la fenetre

continuer = 1

a = 0

#boucle de gestion de la fentre
while continuer:
    for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
        if event.type == QUIT:  # Si un de ces evenements est de type QUIT
            continuer = 0  # On arrete la boucle
            argent.stopper()
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
            if a == 0 :
                print("ouvre la boutique")
                a = 1
                pygame.display.flip()
            elif a == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
                a = 0
                print("ferme la boutique")
        elif a == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_2.collidepoint(
                event.pos):
            print("x2")
        elif a == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_5.collidepoint(
                event.pos):
            print("x5")
        elif a == 1 and event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique_mod_10.collidepoint(
                event.pos):
            print("x10")
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
            print("ouvre menu monstre")
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
            print("ouvre inventaire")

    #permet de reactualiser le fond
    fenetre.blit(fond, (0, 0))
    fenetre.blit(ombre, (x_ombre, y_ombre))
    fenetre.blit(fond_donee, (0, 0))
    fenetre.blit(button_boutique, (30, 570))
    fenetre.blit(button_menu_monstre, (220, 570))
    fenetre.blit(button_inventaire, (460, 570))

    #fenetre.blit(affiche_menu_boutique, ())
    afficher_menu(a, fenetre)

    #afficher l'heure
    font = pygame.font.Font("Vogue.ttf", 20)  # Police principale
    heure = datetime.now()
    heure_1 = heure.strftime("%H:%M:%S")
    heure_a_afficher = font.render(heure_1, True, (0, 0, 0),)
    heure_a_afficher_sans_fond = heure_a_afficher.convert_alpha()
    fenetre.blit(heure_a_afficher, (10, 40))

    #afficher la date
    font = pygame.font.Font("Vogue.ttf", 20)
    date = date.today()
    date_1 = date.strftime("%d/%m/%Y")
    date_a_afficher = font.render(date_1, True, (0, 0, 0))
    date_a_afficher_sans_fond = date_a_afficher.convert_alpha()
    fenetre.blit(date_a_afficher_sans_fond, (10, 10))


    #afficher l'argent
    font = pygame.font.Font("Vogue.ttf", 20)
    argent_a_afficher = font.render("Votre argent : " + str(argent.compteur), True, (0, 0, 0),)
    argent_a_afficher_sans_fond = argent_a_afficher.convert_alpha()
    fenetre.blit(argent_a_afficher, (35, 100))

    #gere l'actualisation de l'heure
    pygame.display.flip()
    horloge.tick(60)
