import pygame
import sys
from LiteratureWork import *
clock = pygame.time.Clock()
class Button:
    def __init__(self, x, y, w, l, txt, color, txt_str = ""):
        self.rect = pygame.Rect(x, y, w, l)
        self.txt = txt
        self.color = color
        self.txt_str = txt_str
    def createButton(self, x_gap, y_gap, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt, (self.rect.x + x_gap, self.rect.y + y_gap))

#xem chu dau cua 2 string co giong nhau ko
def checkString(s1, s2):
    l1 = s1.split()
    l2 = s2.split()
    if(l1[0].casefold() == l2[0].casefold()):
        return True
    return False