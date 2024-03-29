import sys
import time
import pygame
import random
from Utils import *
from LiteratureWork import Work

from mySQLConn import connect

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    # do dai, rong window
    width = 1200
    height = 750
    # man hinh chinh
    screen = pygame.display.set_mode([width, height])
    base_font = pygame.font.SysFont(None, 30)
    smaller_font = pygame.font.SysFont(None, 18)
    smaller_cfont = pygame.font.SysFont(None, 24)
    # cac bai
    works = connect()
    # cac bai da doan
    guesses = []

    # lua chon dap an dung
    # winner = works[random.randint(0, len(works) - 1)]
    winner = works[15]
    suggestions = []

    background = pygame.image.load("images/background.jpg")
    background = pygame.transform.scale(background,(1200,750))
    arrow = pygame.image.load("images/uparrow.png")
    up_arrow = pygame.transform.scale(arrow, (30,30))
    down_arrow = pygame.transform.flip(up_arrow, True, True)
    htp_img = pygame.image.load("images/howtoplay.png")
    htp_img = pygame.transform.scale(htp_img, (1200,750))

    # cac man hinh
    def play():
        user_text = ''
        input_rect = pygame.Rect(25, 100, 1100, 50)
        while True:
            command = base_font.render("Nhap ten 1 tac pham:", True, (169, 252, 3))
            play_back_button = Button(975, 30, 125, 50, base_font.render("Tro Ve", True, (0, 0, 0)), (169, 252, 3))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back_button.rect.collidepoint(event.pos):
                        main_menu()
                    for s in suggestions:
                        if s.rect.collidepoint(event.pos):
                            user_text = s.txt_str
                            if (user_text.casefold() == winner.name.casefold()):
                                win_screen(winner)
                            else:
                                guesses.append(user_text)
                                if len(guesses) > 6:
                                    win_screen(winner)
                            user_text = ''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if(user_text.casefold() == winner.name.casefold()):
                            win_screen(winner)
                        else:
                            guesses.append(user_text)
                            if len(guesses) > 6:
                                win_screen(winner)
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(command, (150, 25))
            guess_num = base_font.render("Luot doan: " + str(len(guesses) + 1) + "/8", True, (169, 252, 3))
            screen.blit(guess_num, (150,60))
            play_back_button.createButton(30, 15, screen)

            # xu li bai doan
            y = 200
            for guess in guesses:
                for work in works:
                    if (guess.casefold() == work.name.casefold()):
                        displayGuess(work, y)
                        y += 50

            pygame.draw.rect(screen, (255,255,255), input_rect)
            text_surface = base_font.render(user_text, True, (0,0,0))
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            #du doan dap an
            suggestions.clear()
            if user_text:
                y1 = 150
                for work in works:
                    if work.name.casefold().startswith(user_text):
                        suggestions.append(Button(25, y1, 1100, 50, base_font.render(work.name, True, (255, 255, 255)), (50, 50, 50), work.name))
                        y1 += 50
                        if(len(suggestions) > 4):
                            break
                for s in suggestions:
                    s.createButton(10,22, screen)
            pygame.display.flip()
            clock.tick(60)

    def win_screen(work):
        guesses.clear()
        suggestions.clear()
        global winner
        winner = works[random.randint(0, len(works) - 1)]
        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(base_font.render(u"Ten", True, (255, 255, 255)), (100, 50))
            screen.blit(base_font.render(u"Nam xuat ban", True, (255, 255, 255)), (300, 50))
            screen.blit(base_font.render(u"Lop", True, (255, 255, 255)), (475, 50))
            screen.blit(base_font.render(u"The loai", True, (255, 255, 255)), (550, 50))
            screen.blit(base_font.render(u"Nam sinh", True, (255, 255, 255)), (700, 50))
            screen.blit(base_font.render(u"Nam mat", True, (255, 255, 255)), (850, 50))
            screen.blit(base_font.render(u"Que", True, (255, 255, 255)), (1000, 50))
            screen.blit(base_font.render(u"Tac gia:", True, (255, 255, 255)), (100, 160))

            guesss_rect = pygame.Rect(25, 85, 1100, 50)
            pygame.draw.rect(screen, (50, 50, 50), guesss_rect)

            if len(work.name) < 19:
                screen.blit(base_font.render(work.name, True, (255, 255, 255)), (50, 100))
            else:
                screen.blit(smaller_font.render(work.name, True, (255, 255, 255)), (50,100))
            screen.blit(base_font.render(str(work.year), True, (255, 255, 255)), (310, 100))
            screen.blit(base_font.render(str(work.grade), True, (255, 255, 255)), (475, 100))
            if len(work.category) < 11:
                screen.blit(base_font.render(work.category, True, (255, 255, 255)), (550, 100))
            else:
                screen.blit(smaller_cfont.render(work.category, True, (255, 255, 255)), (550, 100))
            screen.blit(base_font.render(str(work.author_birth), True, (255, 255, 255)), (700, 100))
            screen.blit(base_font.render(str(work.author_death), True, (255, 255, 255)), (850, 100))
            screen.blit(base_font.render(str(work.author_home), True, (255, 255, 255)), (1000, 100))
            screen.blit(base_font.render(work.author_name, True, (255, 255, 255)), (180, 160))

            play_again_button = Button(720, 440, 200, 50, base_font.render("Choi lan nua", True, (0, 0, 0)), (169, 252, 3))
            play_again_button.createButton(35, 15, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.rect.collidepoint(event.pos):
                        play()

            content = pygame.image.load(work.img)
            content = pygame.transform.scale(content, (500,500))
            screen.blit(content, (50,200))
            pygame.display.flip()

    def htp():
        while True:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            screen.blit(htp_img, (0,0))
            htp_back_button = Button(975, 30, 125, 50, base_font.render("Tro Ve", True, (0, 0, 0)), (169, 252, 3))
            htp_back_button.createButton(30, 15, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if htp_back_button.rect.collidepoint(event.pos):
                        main_menu()
            pygame.display.flip()

    def main_menu():
        guesses.clear()
        suggestions.clear()
        while True:
            screen.fill((255, 255, 255))
            screen.blit(background,(0, 0))
            play_button = Button(475, 250, 250, 50, base_font.render("Choi", True,  (0, 0, 0)), (169, 252, 3))
            htp_button = Button(475, 325, 250, 50, base_font.render("Cach choi", True, (0, 0, 0)), (169, 252, 3))
            quit_button = Button(475, 400, 250, 50, base_font.render("Thoat", True, (0, 0, 0)), (169, 252, 3))
            play_button.createButton(100, 15, screen)
            htp_button.createButton(80, 15, screen)
            quit_button.createButton(100, 15, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if htp_button.rect.collidepoint(event.pos):
                        htp()
                    if play_button.rect.collidepoint(event.pos):
                        play()
                    if quit_button.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.flip()

    #hien thi nhung bai da doan
    def displayGuess(work, y):
        #display o tren
        screen.blit(base_font.render(u"Ten", True, (255,255,255)), (100, 170))
        screen.blit(base_font.render(u"Nam xuat ban", True, (255,255,255)), (300, 170))
        screen.blit(base_font.render(u"Lop", True, (255,255,255)), (475, 170))
        screen.blit(base_font.render(u"The loai", True, (255,255,255)), (550, 170))
        screen.blit(base_font.render(u"Nam sinh", True, (255,255,255)), (700, 170))
        screen.blit(base_font.render(u"Nam mat", True, (255,255,255)), (850, 170))
        screen.blit(base_font.render(u"Que", True, (255,255,255)), (1000, 170))
        guesss_rect = pygame.Rect(25, y, 1100, 50)
        pygame.draw.rect(screen, (50, 50, 50), guesss_rect)

        # so sanh
        if work.year == winner.year:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(275,y, 140, 50))
        else:
            if abs(work.year - winner.year) <= 100:
                pygame.draw.rect(screen, (240, 252, 3), pygame.Rect(270, y, 140, 50))
            if work.year - winner.year < 0:
                screen.blit(up_arrow, (370, y))
            else:
                screen.blit(down_arrow, (370, y))

        if work.grade == winner.grade:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(450,y, 70, 50))
        else:
            if abs(work.grade - winner.grade) <= 1:
                pygame.draw.rect(screen, (240, 252, 3), pygame.Rect(450, y,70, 50))
            if work.grade - winner.grade < 0:
                screen.blit(up_arrow, (490, y))
            else:
                screen.blit(down_arrow, (490, y))

        if work.category == winner.category:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(525, y, 150, 50))
        elif checkString(work.category, winner.category):
            pygame.draw.rect(screen, (240, 252, 3), pygame.Rect(525, y, 150, 50))

        if work.author_birth == winner.author_birth:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(680,y, 110, 50))
        else:
            if abs(work.author_birth - winner.author_birth) <= 100:
                pygame.draw.rect(screen, (240, 252, 3), pygame.Rect(680, y, 110, 50))
            if work.author_birth - winner.author_birth < 0:
                screen.blit(up_arrow, (760, y))
            else:
                screen.blit(down_arrow, (760, y))

        if work.author_death == winner.author_death:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(810,y, 140, 50))
        else:
            if abs(work.author_death - winner.author_death) <= 100:
                pygame.draw.rect(screen, (240, 252, 3), pygame.Rect(810, y, 140, 50))
            if work.author_death - winner.author_death < 0:
                screen.blit(up_arrow, (910, y))
            else:
                screen.blit(down_arrow, (910, y))

        if work.author_home == winner.author_home:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(950,y, 200, 50))

        #cac dap an
        if len(work.name) < 19:
            screen.blit(base_font.render(work.name, True, (255,255,255)), (50, y + 15))
        else:
            screen.blit(smaller_font.render(work.name, True, (255, 255, 255)), (50, y + 15))
        screen.blit(base_font.render(str(work.year), True, (255,255,255)), (310, y + 15))
        screen.blit(base_font.render(str(work.grade), True, (255, 255, 255)), (475, y + 15))
        if len(work.category) < 11:
            screen.blit(base_font.render(work.category, True, (255,255,255)), (530, y+15))
        else:
            screen.blit(smaller_cfont.render(work.category, True, (255, 255, 255)), (530, y + 15))
        screen.blit(base_font.render(str(work.author_birth), True, (255,255,255)), (700, y+15))
        screen.blit(base_font.render(str(work.author_death), True, (255,255,255)), (850, y+15))
        screen.blit(base_font.render(str(work.author_home), True, (255,255,255)), (1000, y+15))

    main_menu()