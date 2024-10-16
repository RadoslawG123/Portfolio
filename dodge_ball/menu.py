import pygame

class Menu():
    def __init__(self, game):
        super().__init__()
        self.game = game

        ## Title and text
        self.font_1 = pygame.font.SysFont('impact',70)
        self.font_2 = pygame.font.SysFont('impact',160)
        self.title_text1 = self.font_1.render(f"Welcome to", True, (0,0,0))
        self.title_text2 = self.font_2.render(f"Dodge ball!", True, (0,0,0))
        self.title_rect1 = self.title_text1.get_rect(center = (self.game.screen_x/2, self.game.screen_y/5))
        self.title_rect2 = self.title_text1.get_rect(center = (self.title_rect1.centerx/1.35, self.title_rect1.centery*1.4))
        # self.title_rect2 = self.title_text1.get_rect(center = (self.game.screen_x/2.7, self.game.screen_y/3.5)) ## DEBUG

        ## Leaderboard
        self.ranking = []
        self.font = pygame.font.SysFont('impact', 50)
        self.leaderboard_surf = pygame.image.load('images/Others/leaderboard.png').convert_alpha()
        self.leaderboard_surf = pygame.transform.scale(self.leaderboard_surf, (self.game.screen_x/2.5, self.game.screen_y/1.4))
        self.leaderboard_rect = self.leaderboard_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/2.2))

    def buttons(self):
        ## Button: Start
        self.button_1_surf = pygame.image.load('images/Buttons/start1.png').convert_alpha()
        self.button_2_surf = pygame.image.load('images/Buttons/start2.png').convert_alpha()
        self.button_1_rect = self.button_1_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/1.5))
        self.button_2_rect = self.button_2_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/1.5))

        ## Button: Leaderboard
        self.button_3_surf = pygame.image.load('images/Buttons/leaderboard1.png').convert_alpha()
        self.button_4_surf = pygame.image.load('images/Buttons/leaderboard2.png').convert_alpha()
        self.button_3_rect = self.button_3_surf.get_rect(center = (self.button_1_rect.centerx, self.button_1_rect.bottom + 75))
        self.button_4_rect = self.button_4_surf.get_rect(center = (self.button_1_rect.centerx, self.button_1_rect.bottom + 75))

        ## Button: Exit
        self.button_5_surf = pygame.image.load('images/Buttons/exit1.png').convert_alpha()
        self.button_6_surf = pygame.image.load('images/Buttons/exit2.png').convert_alpha()
        self.button_5_rect = self.button_5_surf.get_rect(center = (self.button_3_rect.centerx, self.button_3_rect.bottom + 75))
        self.button_6_rect = self.button_6_surf.get_rect(center = (self.button_3_rect.centerx, self.button_3_rect.bottom + 75))

        ## Button: Back
        self.button_7_surf = pygame.image.load('images/Buttons/back1.png').convert_alpha()
        self.button_8_surf = pygame.image.load('images/Buttons/back2.png').convert_alpha()
        self.button_7_rect = self.button_7_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/1.1))
        self.button_8_rect = self.button_8_surf.get_rect(center = (self.game.screen_x/2, self.game.screen_y/1.1))

        ## Buttons activities
        # Start
        if pygame.Rect.collidepoint(self.button_1_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_2_surf, self.button_2_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(200)
                self.game.option = self.game.button_start_active
        else:
            self.game.screen.blit(self.button_1_surf, self.button_1_rect)
        
        # Leaderboard
        if pygame.Rect.collidepoint(self.button_3_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_4_surf, self.button_4_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(200)
                self.game.option = self.game.button_leaderboard_active
        else:
            self.game.screen.blit(self.button_3_surf, self.button_3_rect)

        # Exit
        if pygame.Rect.collidepoint(self.button_5_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_6_surf, self.button_6_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(200)
                self.game.option = self.game.button_exit_active
        else:
            self.game.screen.blit(self.button_5_surf, self.button_5_rect)

    def leaderboard_show(self):
        self.game.screen.fill((255,255,255))
        self.game.screen.blit(self.leaderboard_surf, self.leaderboard_rect)

        ## Score board
        with open("leaderboard.txt", "r") as file:
            position = 1
            ranking_y = self.leaderboard_rect.top + 50
            for line in file.readlines(): 
                self.game.screen.blit(self.font.render(f"{position}.        {line.strip()}", True, (0,0,0)), (self.leaderboard_rect.centerx/1.1, ranking_y))
                position += 1
                ranking_y += 50

        ## Button: Back - activity
        if pygame.Rect.collidepoint(self.button_7_rect, pygame.mouse.get_pos()):
            self.game.screen.blit(self.button_8_surf, self.button_8_rect)
            if pygame.mouse.get_pressed()[0] == True:
                pygame.time.delay(200)
                self.game.option = self.game.button_back_active 
        else:
            self.game.screen.blit(self.button_7_surf, self.button_7_rect)

    def update(self):
        self.game.screen.blit(self.title_text1, self.title_rect1)
        self.game.screen.blit(self.title_text2, self.title_rect2)
        self.buttons()