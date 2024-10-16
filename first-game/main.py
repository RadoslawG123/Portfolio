import pygame
import os
import random
pygame.font.init()


pygame.display.set_caption("Meteor Game")

WIDTH = 900
HEIGHT = 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

VEL = 10

PLAYER_SPACESHIP_WIDTH = 120
PLAYER_SPACESHIP_HEIGHT = 120
ASTEROIDS_WIDTH = 150 
ASTEROIDS_HEIGHT = 150

BONUS_STAR_WIDTH = 90
BONUS_STAR_HEIGHT = 90
BONUS_STAR_X = WIDTH/2
BONUS_STAR_Y = HEIGHT/2

ASTEROID_RANDOM_PLACE_X_1 = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
ASTEROID_RANDOM_PLACE_X_2 = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
ASTEROID_RANDOM_PLACE_X_3 = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
ASTEROID_RANDOM_PLACE_X_4 = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
ASTEROID_RANDOM_PLACE_X_5 = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
################################# All images and scales of asteroids ###########################################################
ASTEROID_1_IMAGE = pygame.image.load(os.path.join('Assets/asteroid_1.png'))
ASTEROID_1_SCALE = pygame.transform.rotate(pygame.transform.scale(ASTEROID_1_IMAGE, (ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)), 0)
ASTEROID_1 = pygame.Rect(ASTEROID_RANDOM_PLACE_X_1, random.randint(-1000, 0 - ASTEROIDS_HEIGHT), ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)

ASTEROID_2_IMAGE = pygame.image.load(os.path.join('Assets/asteroid_2.png'))
ASTEROID_2_SCALE = pygame.transform.rotate(pygame.transform.scale(ASTEROID_2_IMAGE, (ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)), 0)
ASTEROID_2 = pygame.Rect(ASTEROID_RANDOM_PLACE_X_2, random.randint(-1000, 0 - ASTEROIDS_HEIGHT), ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)

ASTEROID_3_IMAGE = pygame.image.load(os.path.join('Assets/asteroid_3.png'))
ASTEROID_3_SCALE = pygame.transform.rotate(pygame.transform.scale(ASTEROID_3_IMAGE, (ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)), 0)
ASTEROID_3 = pygame.Rect(ASTEROID_RANDOM_PLACE_X_3, random.randint(-1000, 0 - ASTEROIDS_HEIGHT), ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)

ASTEROID_4_IMAGE = pygame.image.load(os.path.join('Assets/asteroid_4.png'))
ASTEROID_4_SCALE = pygame.transform.rotate(pygame.transform.scale(ASTEROID_4_IMAGE, (ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)), 0)
ASTEROID_4 = pygame.Rect(ASTEROID_RANDOM_PLACE_X_4, random.randint(-1000, 0 - ASTEROIDS_HEIGHT), ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)

ASTEROID_5_IMAGE = pygame.image.load(os.path.join('Assets/asteroid_1.png'))
ASTEROID_5_SCALE = pygame.transform.rotate(pygame.transform.scale(ASTEROID_2_IMAGE, (ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)), 180)
ASTEROID_5 = pygame.Rect(ASTEROID_RANDOM_PLACE_X_5, random.randint(-1000, 0 - ASTEROIDS_HEIGHT), ASTEROIDS_WIDTH, ASTEROIDS_HEIGHT)
################################################################################################################################
PLAYER_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets/spaceship.png'))
PLAYER_SPACESHIP_SCALE = pygame.transform.rotate(pygame.transform.scale(PLAYER_SPACESHIP_IMAGE, (PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT)), 180)
PLAYER_SPACESHIP = pygame.Rect(WIDTH/2 - PLAYER_SPACESHIP_WIDTH/2, HEIGHT - PLAYER_SPACESHIP_HEIGHT - 20, PLAYER_SPACESHIP_WIDTH, PLAYER_SPACESHIP_HEIGHT)
PLAYER_SPACESHIP_GET_HIT_1 = pygame.USEREVENT + 1
PLAYER_SPACESHIP_GET_HIT_2 = pygame.USEREVENT + 2
PLAYER_SPACESHIP_GET_HIT_3 = pygame.USEREVENT + 3
PLAYER_SPACESHIP_GET_HIT_4 = pygame.USEREVENT + 4
PLAYER_SPACESHIP_GET_HIT_5 = pygame.USEREVENT + 5
################################################################################################################################
BONUS_STAR_IMAGE = pygame.image.load(os.path.join('Assets/bonus_star.png'))
BONUS_STAR_SCALE = pygame.transform.rotate(pygame.transform.scale(BONUS_STAR_IMAGE, (BONUS_STAR_WIDTH, BONUS_STAR_HEIGHT)), 0)
BONUS_STAR = pygame.Rect(BONUS_STAR_X, BONUS_STAR_Y, BONUS_STAR_WIDTH, BONUS_STAR_HEIGHT)
PLAYER_SPACESHIP_GET_BONUS_STAR = pygame.USEREVENT + 6


BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background.png')), (WIDTH, HEIGHT))

WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)

SCORE_FONT = pygame.font.SysFont('comicsans', 40)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
LOSE_FONT = pygame.font.SysFont('comicsans', 150)

def draw_window(health, score):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(PLAYER_SPACESHIP_SCALE, (PLAYER_SPACESHIP.x, PLAYER_SPACESHIP.y))
    WIN.blit(BONUS_STAR_SCALE, (BONUS_STAR.x, BONUS_STAR.y))
    WIN.blit(ASTEROID_1_SCALE, (ASTEROID_1.x, ASTEROID_1.y))
    WIN.blit(ASTEROID_2_SCALE, (ASTEROID_2.x, ASTEROID_2.y))
    WIN.blit(ASTEROID_3_SCALE, (ASTEROID_3.x, ASTEROID_3.y))
    WIN.blit(ASTEROID_4_SCALE, (ASTEROID_4.x, ASTEROID_4.y))
    WIN.blit(ASTEROID_5_SCALE, (ASTEROID_5.x, ASTEROID_5.y))

    health_text = HEALTH_FONT.render("Health: " + str(health), 1, WHITE)
    WIN.blit(health_text, (10 ,10))

    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    pygame.display.update()

def asteroids_movement():

    global score
    global ASTEROIDS_VEL_1
    global ASTEROIDS_VEL_2
    global ASTEROIDS_VEL_3
    global ASTEROIDS_VEL_4
    global ASTEROIDS_VEL_5

    if ASTEROID_1.y < HEIGHT:
        ASTEROID_1.y += ASTEROIDS_VEL_1
    else: 
        ASTEROID_1.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
        ASTEROID_1.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
        ASTEROIDS_VEL_1 = random.randint(8, 15)
        score += 1

    if ASTEROID_2.y < HEIGHT:
        ASTEROID_2.y += ASTEROIDS_VEL_2
    else: 
        ASTEROID_2.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
        ASTEROID_2.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
        ASTEROIDS_VEL_2 = random.randint(8, 15)
        score += 1

    if ASTEROID_3.y < HEIGHT:
        ASTEROID_3.y += ASTEROIDS_VEL_3
    else: 
        ASTEROID_3.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
        ASTEROID_3.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
        ASTEROIDS_VEL_3 = random.randint(8, 15)
        score += 1

    if ASTEROID_4.y < HEIGHT:
        ASTEROID_4.y += ASTEROIDS_VEL_4
    else: 
        ASTEROID_4.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
        ASTEROID_4.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
        ASTEROIDS_VEL_4 = random.randint(8, 15)
        score += 1

    if ASTEROID_5.y < HEIGHT:
        ASTEROID_5.y += ASTEROIDS_VEL_5
    else: 
        ASTEROID_5.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
        ASTEROID_5.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
        ASTEROIDS_VEL_5 = random.randint(8, 15)
        score += 1

def player_movement(keys_pressed, PLAYER_SPACESHIP):
    if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and PLAYER_SPACESHIP.x > 0:
        PLAYER_SPACESHIP.x -= VEL
    if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and PLAYER_SPACESHIP.x < WIDTH - PLAYER_SPACESHIP.width:
        PLAYER_SPACESHIP.x += VEL
    if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and PLAYER_SPACESHIP.y > 0:
        PLAYER_SPACESHIP.y -= VEL
    if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and PLAYER_SPACESHIP.y < HEIGHT - PLAYER_SPACESHIP.height:
        PLAYER_SPACESHIP.y += VEL

    if PLAYER_SPACESHIP.colliderect(ASTEROID_1):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_HIT_1))
    if PLAYER_SPACESHIP.colliderect(ASTEROID_2):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_HIT_2))
    if PLAYER_SPACESHIP.colliderect(ASTEROID_3):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_HIT_3))
    if PLAYER_SPACESHIP.colliderect(ASTEROID_4):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_HIT_4))
    if PLAYER_SPACESHIP.colliderect(ASTEROID_5):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_HIT_5))
    if PLAYER_SPACESHIP.colliderect(BONUS_STAR):
            pygame.event.post(pygame.event.Event(PLAYER_SPACESHIP_GET_BONUS_STAR))
    

def draw_a_lose(text):
    lose = LOSE_FONT.render(text, 1, WHITE)
    WIN.blit(lose, (WIDTH/2 - lose.get_width()/2, HEIGHT/2 - lose.get_height()/2))

    pygame.display.update()

def main():
    health = 10

    global score
    score = 0

    global ASTEROIDS_VEL_1
    global ASTEROIDS_VEL_2
    global ASTEROIDS_VEL_3
    global ASTEROIDS_VEL_4
    global ASTEROIDS_VEL_5

    ASTEROIDS_VEL_1 = random.randint(8, 15)
    ASTEROIDS_VEL_2 = random.randint(8, 15)
    ASTEROIDS_VEL_3 = random.randint(8, 15)
    ASTEROIDS_VEL_4 = random.randint(8, 15)
    ASTEROIDS_VEL_5 = random.randint(8, 15)

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == PLAYER_SPACESHIP_GET_HIT_1:
                ASTEROIDS_VEL_1 = random.randint(8, 15)
                ASTEROID_1.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
                ASTEROID_1.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
                health -= 1
            if event.type == PLAYER_SPACESHIP_GET_HIT_2:
                ASTEROIDS_VEL_2 = random.randint(8, 15)
                ASTEROID_2.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
                ASTEROID_2.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
                health -= 1
            if event.type == PLAYER_SPACESHIP_GET_HIT_3:
                ASTEROIDS_VEL_3 = random.randint(8, 15)
                ASTEROID_3.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
                ASTEROID_3.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
                health -= 1
            if event.type == PLAYER_SPACESHIP_GET_HIT_4:
                ASTEROIDS_VEL_4 = random.randint(8, 15)
                ASTEROID_4.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
                ASTEROID_4.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
                health -= 1
            if event.type == PLAYER_SPACESHIP_GET_HIT_5:
                ASTEROIDS_VEL_5 = random.randint(8, 15)
                ASTEROID_5.y = random.randint(-600, 0 - ASTEROIDS_HEIGHT)
                ASTEROID_5.x = random.randint(0, WIDTH - ASTEROIDS_WIDTH)
                health -= 1
            if event.type == PLAYER_SPACESHIP_GET_BONUS_STAR:
                BONUS_STAR_HISTORY_X = BONUS_STAR.x
                BONUS_STAR_HISTORY_Y = BONUS_STAR.y
                BONUS_STAR.x = random.randint(0, WIDTH - BONUS_STAR_WIDTH) 
                BONUS_STAR.y = random.randint(150, 300)
                print("X:",BONUS_STAR_HISTORY_X)
                print("Y:",BONUS_STAR_HISTORY_Y)
                score += 10

        if health <= 0:
            winner_text = "You Lose!"
            draw_a_lose(winner_text)
            pygame.time.delay(3500)
            pygame.quit()

        keys_pressed = pygame.key.get_pressed()
    
        player_movement(keys_pressed, PLAYER_SPACESHIP)
        asteroids_movement()
        draw_window(health, score)
        

if __name__ == "__main__":
    main()