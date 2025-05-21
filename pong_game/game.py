import pygame
from paddle import Paddle
from ball import Ball

def run_game(mode):
    if not pygame.get_init():
        pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    
    # Objekter 
    paddle_width, paddle_height = 10, 100
    speed = 6
    ball_speed = 5

    paddle1 = Paddle(30, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height, speed)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height, speed)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 15, ball_speed)

    # Sætter Score for begge spillere
    score_p1 = 0
    score_p2 = 0
    max_score = 5

    game_over = False
    winner = None
    
    while True:
        screen.fill((0, 0, 0))
        
        if not game_over:
            # Tegner paddles, bold og score
            pygame.draw.rect(screen, (255, 255, 255), paddle1.rect)
            pygame.draw.rect(screen, (255, 255, 255), paddle2.rect)
            pygame.draw.ellipse(screen, (255, 255, 255), ball.rect)
            pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)

            # Input for spiller 1 (w/s)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle1.move(up=True)
            if keys[pygame.K_s]:
                paddle1.move(up=False)

            # Input for spiller 2 / Ai (op/ned)
            if mode == "2 Players":
                if keys[pygame.K_UP]:
                    paddle2.move(up=True)
                if keys[pygame.K_DOWN]:
                    paddle2.move(up=False)
            elif mode == "vs AI":
                if ball.rect.centery < paddle2.rect.centery:
                    paddle2.move(up=True)
                elif ball.rect.centery > paddle2.rect.centery:
                    paddle2.move(up=False)

            # Boldens bevægelse
            ball.update()

            # Bold-kollision med paddles
            if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
                ball.speed_x = -ball.speed_x
        
            # Score-logik og boldens position reset
            if ball.rect.left < 0:
                score_p2 += 1
                ball.reset(WIDTH // 2, HEIGHT // 2)
            elif ball.rect.right > WIDTH:
                score_p1 += 1
                ball.reset(WIDTH // 2, HEIGHT // 2)

            # Tegn score
            score_text = font.render(f"Player 1: {score_p1}  Player 2: {score_p2}", True, (255, 255, 255))
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

            # Tjek for vinderen
            if score_p1 >= max_score or score_p2 >= max_score:
                winner = "Player 1" if score_p1 >= max_score else "Player 2"
                win_text = font.render(f"{winner} wins!", True, (255, 255, 255))
                info_text = font.render("Press R to restart or ESC to exit", True, (255, 255, 255))

                screen.fill((0, 0, 0))
                screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 60))
                screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT // 2))
                pygame.display.flip()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return run_game(mode)
                            elif event.key == pygame.K_ESCAPE:
                                return pygame.quit()


        # Event-håndtering
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.flip()
        clock.tick(60)
        

