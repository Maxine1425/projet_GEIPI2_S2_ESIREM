import pygame
from pygame.locals import *
from datetime import datetime
from datetime import date
import afficher_heure
from time import strftime
pygame.init()

fenetre = pygame.display.set_mode((990, 660),) #creation de la fenetre

pygame.display.set_caption("Jeux") #nom du jeu apparait

fond = pygame.image.load("fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
fenetre.blit(fond, (0,0)) #on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

button_boutique = pygame.image.load("button_boutique.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_boutique, (30, 570))
button_menu_monstre = pygame.image.load("button_menu-monstre.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_menu_monstre, (220, 570))
button_inventaire = pygame.image.load("button_inventaire.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_inventaire, (460, 570))

# creation des zones de click
clickable_area_boutique = pygame.Rect((30, 570), (160, 49))
clickable_area_menu_monstre = pygame.Rect((220, 570), (210, 49))
clickable_area_inventaire = pygame.Rect((460, 570), (168, 49))

#creation de l'orloge pour afficher l'heure
horloge = pygame.time.Clock()



pygame.display.flip() #ligne pour gerer le rafraichissement de la fenetre

continuer = 1

while continuer: #boucle pour que la fenetre reste ouverte
    for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
        if event.type == QUIT:  # Si un de ces evenements est de type QUIT
            continuer = 0  # On arrete la boucle
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_boutique.collidepoint(event.pos):
           print("ouvre la boutique")
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_menu_monstre.collidepoint(event.pos):
            print("ouvre menu monstre")
        elif event.type == MOUSEBUTTONUP and event.button == 1 and clickable_area_inventaire.collidepoint(event.pos):
            print("ouvre inventaire")
    #afficher l'heure
    font = pygame.font.Font(None, 36)  # Police principale
    heure = datetime.now()
    heure_1 = heure.strftime("%H:%M:%S")
    heure_a_afficher = font.render(heure_1, True, (0, 0, 0), (167, 209, 239))
    fenetre.blit(heure_a_afficher, (10, 40))

    #afficher la date
    font = pygame.font.Font(None, 36)
    date = date.today()
    date_1 = date.strftime("%d/%m/%Y")
    date_a_afficher = font.render(date_1, True, (0, 0, 0), (167, 209, 239))
    fenetre.blit(date_a_afficher, (10, 10))

    #gere l'actualisation de l'heure
    pygame.display.flip()
    horloge.tick(60)
