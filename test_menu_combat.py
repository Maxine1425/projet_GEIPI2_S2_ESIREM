import time
import Battle
import Monstre
import pygame
from pygame.locals import *
from Money import Compteur

argent = Compteur()
argent.demarrer()

pygame.init()

BLANC = (255,255,255)
NOIR = (0,0,0)
fenetre = pygame.display.set_mode((990, 660),) #creation de la fenetre
x = 990/2
y = 660/2

fond = pygame.image.load("images/fond_menu.png").convert() #on ajoute a fond une image j'utilise .convert pour etre sur qu'elle soit toujours au bon format
fenetre.blit(fond, (0,0)) #on colle sur la fenetre l'image fond et l'angle haut gauche de cette image sera en (0;0)

salameche = pygame.image.load("images/Salameche.png").convert_alpha()
bulbizarre = pygame.image.load("images/Bulbizarre.png").convert_alpha()
hpbarfull = pygame.image.load("images/VIE_FULL.png")
hpbar45 = pygame.image.load("images/VIEQC.png")
hpbar35 = pygame.image.load("images/VIETC.png")
hpbar25 = pygame.image.load("images/VIEDC.png")
hpbar15 = pygame.image.load("images/VIEUC.png")
hpbarempty = pygame.image.load("images/VIE_EMPTY.png")

floor1 = pygame.image.load("images/battlefloor.png")
floor2 = pygame.image.load("images/battlefloor.png")

pressed = pygame.key.get_pressed()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    fenetre.blit(img, (x,y))

text_font = pygame.font.SysFont("Arial", 160)

continuer = 1
compteur = 0
while continuer: #boucle pour que la fenetre reste ouverte

    for event in pygame.event.get():  # On parcours la liste de tous les evenements recus
        if event.type == QUIT:  # Si un de ces evenements est de type QUIT
            continuer = 0  # On arrete la boucle
            argent.stopper()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre la boutique")
            argent.ajouter_mod(15)
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre menu monstre")
            argent.soustraire(50)
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            print("ouvre inventaire")


    # fenetre.fill(BLANC)
    fenetre.blit(fond, (0, 0))

    fenetre.blit(floor1, (600, 200))
    fenetre.blit(floor2, (50, 350))
    fenetre.blit(bulbizarre, (620, 150))
    fenetre.blit(salameche, (70, 300))
    fenetre.blit(hpbarfull, (70, 450))

    pygame.display.flip()
    print(argent.compteur)
