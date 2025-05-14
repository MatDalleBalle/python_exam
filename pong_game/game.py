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
    score1 = 0
    score2 = 0

    running = True
    while running:
        screen.fill((0, 0, 0))

        # Tegner en midterlinje
        for y in range(0, HEIGHT, 20):
            if y % 40 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 1, y, 2, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # input håndtering (spiller 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down(HEIGHT)
        
        # input håndtering (spiller 2 eller AI)
        if mode == "2player":
            if keys[pygame.K_UP]:
                paddle2.move_up()
            if keys[pygame.K_DOWN]:
                paddle2.move_down(HEIGHT)
        else:
            # AI logik for paddle2
            if ball.rect.centery < paddle2.rect.centery:
                paddle2.move_up()
            elif ball.rect.centery > paddle2.rect.centery:
                paddle2.move_down(HEIGHT)

        # Opdatering af boldens position
        ball.update(WIDTH, HEIGHT)

        # Kollision mellem bold og paddles
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        # score (reset bolden)
        if ball.rect.left <= 0:
            score2 += 1
            ball.reset(WIDTH // 2, HEIGHT // 2)
        
        if ball.rect.right >= WIDTH:
            score1 += 1
            ball.reset(WIDTH // 2, HEIGHT // 2)

        # Check for vinder
        if score1 >= 5 or score2 >= 5:
            winner = "Player 1" if score1 >= 5 else "Player 2"
            win_text = font.render(f"{winner}", True, (255, 255, 255))
        
        # Viser objekter
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        # Viser score
        score_text = font.render(f"{score1} - {score2}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 40, 20))


        pygame.display.flip()
        clock.tick(60)

    # efter spillet: spil igen eller menu
    screen.fill((0, 0, 0))
    msg = font.render("Tryk R for at spille igen eller Q for at afslutte", True, (255, 255, 255))
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 24))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_q:
                    return
    
