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

# def displayGuess(work):
#     guesss_rect = pygame.Rect(350,150,950,50)
#     base_font = pygame.font.Font(None, 50)

# #cac man hinh
# def play(screen):
#     #cac bai
#     works = []
#     #cac bai da doan
#     guesses = []
#     #vi du
#     works.append(Work("Co To", 1976, 1910, 1987, "Ha Noi"))
#
#     base_font = pygame.font.Font(None, 50)
#     user_text = ''
#     input_rect = pygame.Rect(150, 150, 950, 50)
#     while True:
#         command = base_font.render("Enter an animal name:", True, (0, 0, 0))
#         play_back_button = Button(800, 30, 250, 50, base_font.render("Back", True, (0, 0, 0)), (0, 0, 255))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if play_back_button.rect.collidepoint(event.pos):
#                     main_menu(screen)
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     guesses.append(user_text)
#                     user_text = ''
#                 elif event.key == pygame.K_BACKSPACE:
#                     user_text = user_text[:-1]
#                 else:
#                     user_text += event.unicode
#         screen.fill((255, 255, 255))
#         screen.blit(command, (425, 100))
#         play_back_button.createButton(25, 10, screen)
#
#         #xu li bai doan
#         for guess in guesses:
#             for work in works:
#                 if(guess == work.name):
#                     displayGuess(work)
#
#         pygame.draw.rect(screen, (0,0,255), input_rect)
#         text_surface = base_font.render(user_text, True, (255, 255, 255))
#         screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
#         # print(user_text)
#         pygame.display.flip()
#         clock.tick(60)
# def htp(screen):
#     while True:
#         screen.fill((255,255,255))
#         base_font = pygame.font.Font(None, 50)
#         htp_back_button = Button(700, 420, 150, 50, base_font.render("Back", True, (0, 0, 0)), (0, 0, 255))
#         htp_back_button.createButton(25,10,screen)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if htp_back_button.rect.collidepoint(event.pos):
#                     main_menu(screen)
#         pygame.display.flip()
# def main_menu(screen):
#     while True:
#         screen.fill((255,255,255))
#         base_font = pygame.font.Font(None, 50)
#         play_button = Button(100, 30, 250, 50, base_font.render("Play", True, (0, 0, 0)), (255, 255, 0))
#         htp_button = Button(800, 30, 250, 50, base_font.render("How to play", True, (0, 0, 0)), (255, 255, 0))
#         play_button.createButton(5,5, screen)
#         htp_button.createButton(22, 10, screen)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if htp_button.rect.collidepoint(event.pos):
#                     htp(screen)
#                 if play_button.rect.collidepoint(event.pos):
#                     play(screen)
#         pygame.display.flip()

