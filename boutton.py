import pygame


class Button:
    """
    Classe permettant de créer des boutons et de gérer les fonctionnalités.
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
