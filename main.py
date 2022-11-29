import time
import pygame
from Utils import *
from LiteratureWork import Work
if __name__ == '__main__':
    pygame.init()
    # dat ten chuong trinh
    pygame.display.set_caption("Anidle")
    # do dai, rong window
    width = 1200
    height = 600
    clock = pygame.time.Clock()
    # man hinh chinh
    screen = pygame.display.set_mode([width, height])
    main_menu(screen)
    # base_font = pygame.font.Font(None, 50)
    # #tao cac nut
    # htp_button = Button(800, 30, 250, 50 , base_font.render("How to play",True,(0,0,0)), (255,255,0))
    # htp_back_button = Button(700, 420, 150, 50, base_font.render("Back", True, (0, 0, 0)), (0, 0, 255))
    # user_text = ''
    # command = base_font.render("Enter an animal name:",True,(0,0,0))
    # htp_window = pygame.Rect(50, 50, 1100, 500)
    # htp_rect_clicked = False
    # htp_back_clicked = True
    # input_rect = pygame.Rect(150, 150, 950, 50)
    # color = (0,0,255)
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #              if htp_button.rect.collidepoint(event.pos):
    #                 #them phan hien len huong dan
    #                 htp_rect_clicked = True
    #                 htp_back_clicked = False
    #              if htp_back_button.rect.collidepoint(event.pos):
    #                 htp_rect_clicked = False
    #                 htp_back_clicked = True
    #                 print("in")
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_BACKSPACE:
    #                 user_text = user_text[:-1]
    #             else:
    #                 user_text += event.unicode
    #     if htp_back_clicked:
    #         screen.fill((255, 255, 255))
    #         screen.blit(command, (425, 100))
    #         htp_button.createButton(22, 10, screen)
    #         pygame.draw.rect(screen, color, input_rect)
    #         text_surface = base_font.render(user_text, True, (255, 255, 255))
    #         screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    #     if htp_rect_clicked:
    #         pygame.draw.rect(screen, (100, 100, 100), htp_window, 0)
    #         htp_back_button.createButton(25, 10, screen)
    #     pygame.display.flip()
    #     print(user_text)
    #     clock.tick(60)
    # pygame.quit()