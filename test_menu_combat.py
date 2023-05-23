import time
import Battle
import Monstre
import pygame
from pygame.locals import *


pygame.init()

BLANC = (255,255,255)
NOIR = (0,0,0)
fenetre = pygame.display.set_mode((990, 660),) #creation de la fenetre
x = 990/2
y = 660/2

fond = pygame.image.load("fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
fenetre.blit(fond, (0,0)) #on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

salameche = pygame.image.load("Salameche.png").convert_alpha()
bulbizarre = pygame.image.load("Bulbizarre.png").convert_alpha()
floor1 = pygame.image.load("battlefloor.png")
floor2 = pygame.image.load("battlefloor.png")

pressed = pygame.key.get_pressed()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    fenetre.blit(img, (x,y))

text_font = pygame.font.SysFont("Arial", 160)

# testmnstr_attaque = Monstre.Monstre("Salameche", 10, "Attaque") #Creation de Salameche, de rarete 10 et de type Attaque
# testmnstr_defense = Monstre.Monstre("Bulbizarre", 10, "Defense") #Creation de Bulbizarre, de rarete 10 et de type Defense
# combat = Battle.Battle(testmnstr_attaque,testmnstr_defense)

continuer = 1
compteur = 0
while continuer: #boucle pour que la fenetre reste ouverte

    for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
        if event.type == QUIT:  # Si un de ces evenements est de type QUIT
            continuer = 0  # On arrete la boucle
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre la boutique")
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre menu monstre")
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre inventaire")


    # fenetre.fill(BLANC)
    fenetre.blit(fond, (0, 0))
    compteur+=1
    font = pygame.font.Font(None, 36)
    texte = font.render(str(compteur), True, NOIR)
    rect = texte.get_rect()
    rect.centerx = x
    rect.centery = y
    fenetre.blit(texte, rect)

    fenetre.blit(floor1, (600, 200))
    fenetre.blit(floor2, (50, 350))
    fenetre.blit(bulbizarre, (620, 150))
    fenetre.blit(salameche, (70, 300))

    pygame.display.flip()

