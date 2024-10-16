import pygame

class Endscreen():
    def __init__(self, game):
        super().__init__()
        self.game = game 

        ## IMAGE
        img_surf = pygame.image.load("images/Player/dead_ball1.png").convert_alpha()
        self.img_surf = pygame.transform.scale(img_surf, (self.game.screen_x/7, self.game.screen_x/7))
        self.img_rect = self.img_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/2))
        
        ## TEXT
        self.font = pygame.font.SysFont('impact', 160)
        self.score_font = pygame.font.SysFont('impact', 40)
        self.text = self.font.render("You lose!", True, (0,0,0))
        self.text_rect = self.text.get_rect(center = (self.game.screen_x/2, self.game.screen_y/6))
        self.score_text = self.score_font.render(f"Your score: {self.game.last_score}", True, (0,0,0))
        self.score_text_rect = self.score_text.get_rect(center = (self.text_rect.centerx, self.text_rect.bottom + 20))

    def buttons(self):
        ## Button: Play Again
        self.button_1_surf = pygame.image.load('images/Buttons/playAgain1.png').convert_alpha()
        self.button_2_surf = pygame.image.load('images/Buttons/playAgain2.png').convert_alpha()
        self.button_1_rect = self.button_1_surf.get_rect(center = (self.img_rect.centerx, self.img_rect.bottom + 100))
        self.button_2_rect = self.button_2_surf.get_rect(center = (self.img_rect.centerx, self.img_rect.bottom + 100))

        ## Button: Main Menu
        self.button_3_surf = pygame.image.load('images/Buttons/mainMenu1.png').convert_alpha()
        self.button_4_surf = pygame.image.load('images/Buttons/mainMenu2.png').convert_alpha()
        self.button_3_rect = self.button_3_surf.get_rect(center = (self.img_rect.centerx, self.img_rect.bottom + 225))
        self.button_4_rect = self.button_4_surf.get_rect(center = (self.img_rect.centerx, self.img_rect.bottom + 225))        

        ## Buttons activities
        # Play again
        if pygame.Rect.collidepoint(self.button_1_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_2_surf, self.button_2_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(200)
                self.game.option = self.game.button_playagain_active
        else:
            self.game.screen.blit(self.button_1_surf, self.button_1_rect)

        # Main menu
        if pygame.Rect.collidepoint(self.button_3_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_4_surf, self.button_4_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(300)
                pygame.sprite.Group.empty(self.game.obstacles_group)
                self.game.obstacles.clear() 
                self.game.option = self.game.button_mainmenu_active
        else:
            self.game.screen.blit(self.button_3_surf, self.button_3_rect)

    def update(self):
        self.game.screen.blit(self.text, self.text_rect)
        self.game.screen.blit(self.score_text, self.score_text_rect)
        self.game.screen.blit(self.img_surf, self.img_rect)
        self.buttons()