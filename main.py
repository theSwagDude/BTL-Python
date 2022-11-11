import time
import pygame
from LiteratureWork import Work
if __name__ == '__main__':
    # print(Work(1,1,1,1,1,1))
    pygame.init()
    pygame.display.set_caption("Anidle")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1200, 600])
    base_font = pygame.font.Font(None, 50)
    user_text = ''
    command = base_font.render("Enter an animal name:",True,(0,0,0))
    htp_txt = base_font.render("How to play",True,(0,0,0))
    htp_rect = pygame.Rect(800, 30, 250, 50)
    input_rect = pygame.Rect(150, 150, 950, 50)
    color = (0,0,255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if htp_rect.collidepoint(event.pos):
                    #them phan hien len huong dan
                    print("instruction")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        screen.fill((255, 255, 255))
        screen.blit(command, (425, 100))
        pygame.draw.rect(screen, (255,0,0), htp_rect, 0)
        screen.blit(htp_txt, (htp_rect.x + 22, htp_rect.y + 10))
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.flip()
        clock.tick(60)