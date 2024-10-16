import pygame
from random import choice, randint

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.game = game
        self.player = player

        ## Images and scales
        self.colors = choice(['images/Obstacles/ball2.png', 'images/Obstacles/ball3.png', 'images/Obstacles/ball4.png', 'images/Obstacles/ball5.png', 'images/Obstacles/ball6.png', 'images/Obstacles/ball7.png', 'images/Obstacles/ball8.png']) # choosing random colors
        surf = pygame.image.load(self.colors).convert_alpha()
        self.surf = pygame.transform.scale(surf, (60, 60))
        self.mask = pygame.mask.from_surface(self.surf)

        ## Started position of obstacle (The position is randomazing beacuse of space around the player)
        if self.game.first_obstacle_position:
            self.rect = choice([self.surf.get_rect(topleft = (randint(10, 50), randint(120, self.game.screen_y-120))), self.surf.get_rect(topright = (randint(self.game.screen_x-50, self.game.screen_x-10), randint(120, self.game.screen_y-120)))])
            self.game.first_obstacle_position = False
        else:
            while True:
                self.rect = self.surf.get_rect(center = (randint(120, self.game.screen_x-120), randint(120, self.game.screen_y-120)))
                if not pygame.Rect.colliderect(self.rect, self.player.space_around):
                    break
        

        ## Velocity
        self.vel = randint(3,6)
        self.vel_x = choice([self.vel, self.vel*-1])
        self.vel_y = choice([self.vel, self.vel*-1])
        
        ## Types
        self.ball_type = choice(['straight', 'nostraight', 'nostraight', 'nostraight', 'nostraight']) # chance of nostraight set to 80%
        self.direction = choice(['x','y'])

    def movement(self):
        if self.ball_type == 'straight':
            if self.direction == 'x':
                self.rect.centerx += self.vel
            else:
                self.rect.centery += self.vel

            if self.rect.top <= 0:
                self.rect.top = 0
                self.vel *= -1
            elif self.rect.bottom >= self.game.screen_y:
                self.rect.bottom = self.game.screen_y
                self.vel *= -1
            elif self.rect.right >= self.game.screen_x:
                self.rect.right = self.game.screen_x
                self.vel *= -1
            elif self.rect.left <= 0:
                self.rect.left = 0
                self.vel *= -1
        else:
            self.rect.centerx += self.vel_x
            self.rect.centery -= self.vel_y
    
            if self.rect.bottom >= self.game.screen_y:
                self.rect.bottom = self.game.screen_y
                self.vel_y *= -1
            elif self.rect.top <= 0:
                self.rect.top = 0
                self.vel_y *= -1
            elif self.rect.right >= self.game.screen_x:
                self.rect.right = self.game.screen_x
                self.vel_x *= -1
            elif self.rect.left <= 0:
                self.rect.left = 0
                self.vel_x *= -1
        

    def update(self):
        self.movement()
        self.game.screen.blit(self.surf, self.rect)