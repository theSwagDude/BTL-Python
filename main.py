import time
import pygame
import random
from Utils import *
from LiteratureWork import Work

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    # dat ten chuong trinh
    pygame.display.set_caption("Anidle")
    # do dai, rong window
    width = 1200
    height = 700
    # clock = pygame.time.Clock()
    # man hinh chinh
    screen = pygame.display.set_mode([width, height])
    base_font = pygame.font.SysFont(None, 40)
    # cac bai
    works = []
    # cac bai da doan
    guesses = []
    # vi du
    works.append(Work("Co To", 1976, "Ki", 1910, 1987, "Ha Noi"))
    works.append(Work("Luom", 1975, "Ki", 1910, 1987, "Ha Noi"))
    works.append(Work("Chi Pheo", 1976, "Tho", 1920, 1977, "Bac Ninh"))
    # lua chon dap an dung
    winner = works[0]
    # winner = works[random.randint(0, len(works) - 1)]

    # cac man hinh
    def play():

        user_text = ''
        input_rect = pygame.Rect(150, 150, 950, 50)
        while True:
            command = base_font.render("Enter an animal name:", True, (0, 0, 0))
            play_back_button = Button(800, 30, 250, 50, base_font.render("Back", True, (0, 0, 0)), (0, 0, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back_button.rect.collidepoint(event.pos):
                        main_menu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if(user_text.casefold() == winner.name.casefold()):
                            win_screen(winner)
                        else:
                            guesses.append(user_text)
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            screen.fill((255, 255, 255))
            screen.blit(command, (425, 100))
            play_back_button.createButton(25, 10, screen)

            # xu li bai doan
            y = 250
            for guess in guesses:
                for work in works:
                    if (guess.casefold() == work.name.casefold()):
                        displayGuess(work, y)
                        y += 100

            pygame.draw.rect(screen, (0, 0, 255), input_rect)
            text_surface = base_font.render(user_text, True, (255, 255, 255))
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            # print(user_text)
            pygame.display.flip()
            clock.tick(60)

    def win_screen(work):
        while True:
            screen.fill((255,255,255))
            guesss_rect = pygame.Rect(100, 100, 1050, 50)
            pygame.draw.rect(screen, (0, 0, 255), guesss_rect)
            screen.blit(base_font.render(work.name, True, (0, 0, 0)), (175, 100))
            screen.blit(base_font.render(str(work.year), True, (0, 0, 0)), (400, 100))
            screen.blit(base_font.render(work.category, True, (0, 0, 0)), (550, 100))
            screen.blit(base_font.render(str(work.author_birth), True, (0, 0, 0)), (700, 100))
            screen.blit(base_font.render(str(work.author_death), True, (0, 0, 0)), (850, 100))
            screen.blit(base_font.render(str(work.author_home), True, (0, 0, 0)), (1000, 100))
            play_again_button = Button(700, 420, 300, 50, base_font.render("Play Again", True, (0, 0, 0)), (0, 0, 255))
            play_again_button.createButton(25, 10, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.rect.collidepoint(event.pos):
                        play()
            pygame.display.flip()

    def htp():
        while True:
            screen.fill((255, 255, 255))
            htp_back_button = Button(700, 420, 150, 50, base_font.render("Back", True, (0, 0, 0)), (0, 0, 255))
            htp_back_button.createButton(25, 10, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if htp_back_button.rect.collidepoint(event.pos):
                        main_menu()
            pygame.display.flip()


    def main_menu():
        while True:
            screen.fill((255, 255, 255))
            play_button = Button(100, 30, 250, 50, base_font.render("Play", True, (0, 0, 0)), (255, 255, 0))
            htp_button = Button(800, 30, 250, 50, base_font.render("How to play", True, (0, 0, 0)), (255, 255, 0))
            play_button.createButton(5, 5, screen)
            htp_button.createButton(22, 10, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if htp_button.rect.collidepoint(event.pos):
                        htp()
                    if play_button.rect.collidepoint(event.pos):
                        play()
            pygame.display.flip()

    def displayGuess(work, y):
        #display o tren
        screen.blit(base_font.render(u"Ten", True, (0, 0, 0)), (175, 200))
        screen.blit(base_font.render(u"Nam xuat ban", True, (0, 0, 0)), (300, 200))
        screen.blit(base_font.render(u"The loai", True, (0, 0, 0)), (550, 200))
        screen.blit(base_font.render(u"Nam sinh", True, (0, 0, 0)), (700, 200))
        screen.blit(base_font.render(u"Nam mat", True, (0, 0, 0)), (850, 200))
        screen.blit(base_font.render(u"Que", True, (0, 0, 0)), (1000, 200))
        guesss_rect = pygame.Rect(100, y, 1050, 50)
        pygame.draw.rect(screen, (0, 0, 255), guesss_rect)
        # so sanh
        if work.year == winner.year:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(350,y, 140, 50))
        elif abs(work.year - winner.year) <= 10:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, y, 140, 50))

        if work.category == winner.category:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(500, y, 140, 50))

        if work.author_birth == winner.author_birth:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(650,y, 140, 50))
        elif abs(work.author_birth - winner.author_birth) <= 10:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(650, y, 140, 50))

        if work.author_death == winner.author_death:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(800,y, 140, 50))
        elif abs(work.author_death - winner.author_death) <= 10:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(800, y, 140, 50))

        if work.author_home == winner.author_home:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(950,y, 200, 50))

        #cac dap an

        screen.blit(base_font.render(work.name, True, (0, 0, 0)), (175, y))
        screen.blit(base_font.render(str(work.year), True, (0, 0, 0)), (400, y))
        screen.blit(base_font.render(work.category, True, (0, 0, 0)), (550, y))
        screen.blit(base_font.render(str(work.author_birth), True, (0, 0, 0)), (700, y))
        screen.blit(base_font.render(str(work.author_death), True, (0, 0, 0)), (850, y))
        screen.blit(base_font.render(str(work.author_home), True, (0, 0, 0)), (1000, y))


    main_menu()