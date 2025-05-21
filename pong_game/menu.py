print("Loading menu.py...")

import pygame
from game import run_game

def show_menu():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT = pygame.font.Font(None, 48)


    while True:
        screen.fill((0, 0, 0))

        title = FONT.render("Pong Game", True, (255, 255, 255))
        option1 = FONT.render("Press 1 - 2 Player", True, (255, 255, 255))
        option2 = FONT.render("Press 2 - vs AI", True, (255, 255, 255))
        option3 = FONT.render("Press ESC - Exit", True, (255, 255, 255))

        screen.blit(title, (WIDTH // 2 - 60, 100))
        screen.blit(option1, (WIDTH // 2 - 100, 200))
        screen.blit(option2, (WIDTH // 2 - 100, 260))
        screen.blit(option3, (WIDTH // 2 - 100, 320))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "2 Player"
                elif event.key == pygame.K_2:
                    return "vs AI"
                elif event.key == pygame.K_ESCAPE:
                    return "afslut"

def main():
    while True:
        mode = show_menu()
        if mode == "afslut":
            break
        elif mode == "2 Player":
            run_game("2 Players")
        elif mode == "vs AI":
            run_game("vs AI")    