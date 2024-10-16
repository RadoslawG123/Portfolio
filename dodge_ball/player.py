import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        # self.pos = pygame.mouse.get_pos() ## DEBUG

        ## Variables, images ans scales
        image = pygame.image.load("images/Player/ball1.png").convert_alpha()
        self.surf = pygame.transform.scale(image, (60, 60))
        self.rect = self.surf.get_rect(center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        self.mask = pygame.mask.from_surface(self.surf)
        self.animation_started = False

        ## Space around player for better obstacles spawns
        self.space_around = pygame.Rect(0, 0, self.game.screen_x/1.5, self.game.screen_y/1.5)
    
    def animation(self):
        if self.game.powerups.shield:
            if self.game.timer_3_miliseconds % 2 == 0:
                image = pygame.image.load("images/Player/ball1_s2.png").convert_alpha()
                self.surf = pygame.transform.scale(image, (60, 60))
            else:
                image = pygame.image.load("images/Player/ball1_s.png").convert_alpha()
                self.surf = pygame.transform.scale(image, (60, 60))
        elif self.game.powerups.multiplier:
            if self.game.timer_3_miliseconds % 2 == 0:
                image = pygame.image.load("images/Player/ball1_m.png").convert_alpha()
                self.surf = pygame.transform.scale(image, (60, 60))
            else:
                image = pygame.image.load("images/Player/ball1_m2.png").convert_alpha()
                self.surf = pygame.transform.scale(image, (60, 60))

    def update(self):
        self.rect = self.surf.get_rect(center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        self.space_around.center = (self.rect.centerx, self.rect.centery)

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.game.screen_y:
            self.rect.bottom = self.game.screen_y
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.game.screen_x:
            self.rect.right = self.game.screen_x
            
        self.game.screen.blit(self.surf, self.rect)