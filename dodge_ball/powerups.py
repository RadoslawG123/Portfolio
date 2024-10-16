import pygame
from random import randint, choice

class Powerups(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        ## Types
        self.type = choice(['shield', 'multiplier', 'freeze'])
        match self.type:
            case 'shield':
                self.image = 'images/Powerups/shield.png'
            case 'multiplier':
                self.image = 'images/Powerups/multiplier.png'
            case 'freeze':
                self.image = 'images/Powerups/freeze_2.png'

        ## Variables, images and scales
        self.surf = pygame.image.load(self.image).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (70, 70))
        self.rect = self.surf.get_rect(center = (-1000, -1000))
        self.mask = pygame.mask.from_surface(self.surf)
        self.show = False
        self.shield = False
        self.multiplier = False
        self.freeze = False

        ## Icon
        self.icon = pygame.transform.scale(self.surf, (70, 70))
        self.icon_rect = self.icon.get_rect(center = (50, 50))

        ## Timer
        self.font = pygame.font.SysFont('impact', 70)
        self.text = self.font.render(f"{self.game.timer_2_seconds}", True, (0,0,0))
        self.text_rect = self.text.get_rect(bottomleft = (self.icon_rect.right + 15, self.icon_rect.bottom + 10))

    def update(self):
        if self.show:
            self.game.screen.blit(self.surf, self.rect)

        if self.game.timer_2_active:
            self.text = self.font.render(f"{self.game.timer_2_seconds}", True, (0,0,0))
            self.game.screen.blit(self.text, self.text_rect)
            self.game.screen.blit(self.icon, self.icon_rect)