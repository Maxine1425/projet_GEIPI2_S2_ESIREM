import pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((990, 660),) #creation de la fenetre

fond = pygame.image.load("fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
fenetre.blit(fond, (0,0)) #on cole sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

button_boutique = pygame.image.load("button_boutique.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_boutique, ( 30,570))
button_menu_monstre = pygame.image.load("button_menu-monstre.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_menu_monstre, ( 220,570))
button_inventaire = pygame.image.load("button_inventaire.png").convert_alpha() #l'image sera avec un fond transparant
fenetre.blit(button_inventaire, ( 460,570))

clickable_area_boutique = pygame.Rect((220, 377), (149, 66))
clickable_area_menu_monstre = pygame.Rect((220, 377), (149, 66))
clickable_area_inventaire = pygame.Rect((220, 377), (149, 66))


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