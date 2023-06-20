import pygame


class Button:
    """
    Classe permettant de cr�er des boutons et de g�rer les fonctionnalit�s.
    """
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def dessiner(self, surface):
        surface.blit(self.image, self.rect)

    def est_clique(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
