import pygame
from random import randint, choice

class Rainbow_rect(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        
        ## Variables, images and scales
        self.color = choice(['green', 'red', 'blue', 'yellow', 'pink'])
        surf = pygame.image.load('images/Bonus/rainbow_rect.png').convert_alpha()
        self.surf = pygame.transform.scale(surf, (30, 30))
        self.rect = self.surf.get_rect(center = (randint(60, self.game.screen_sizes[0][0]-60), randint(60, self.game.screen_sizes[0][1]-60)))
        self.mask = pygame.mask.from_surface(self.surf)
        
    def update(self):
        self.game.screen.blit(self.surf, self.rect)