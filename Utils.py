import pygame
class Button:
    def __init__(self, x, y, w, l, txt, color):
        self.rect = pygame.Rect(x, y, w, l)
        self.txt = txt
        self.color = color
    def createButton(self, x_gap, y_gap, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt, (self.rect.x + x_gap, self.rect.y + y_gap))