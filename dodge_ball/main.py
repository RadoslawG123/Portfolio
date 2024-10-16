import pygame
from sys import exit
from random import randint, choice
from menu import Menu
from end_screen import Endscreen
from player import Player
from rainbow_rect import Rainbow_rect
from obstacles import Obstacles
from powerups import Powerups

## Basic game setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("Dodge Ball Game")

## Timers 
timer_1 = pygame.USEREVENT
timer_2 = pygame.USEREVENT + 1
timer_3 = pygame.USEREVENT + 2
pygame.time.set_timer(timer_1, 1000)
pygame.time.set_timer(timer_2, 1000)
pygame.time.set_timer(timer_3, 100)

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        ## Screen setup and helpful resize screen for easier programming
        self.screen_sizes = pygame.display.get_desktop_sizes()
        self.screen_sizes[0] = list(self.screen_sizes[0])
        # self.screen_resize() ## DEBUG

        for i in self.screen_sizes[0]:
            self.screen_x = self.screen_sizes[0][0]
            self.screen_y = self.screen_sizes[0][1]

        self.screen = pygame.display.set_mode(self.screen_sizes[0]) # Full screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont('impact',60)

        self.normal_color = (255,255,255)
        self.freeze_color = (200,255,255)
        self.screen_color = self.normal_color

        ## Others
        # clock, fps, score, leaderboard
        self.game_active = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.score = 0
        self.last_score = 0
        self.score_5 = 5
        self.leaderboard_flag = False

        # obstacles
        self.obstacles_counter = 0
        self.obstacles_vel_storage = []
        self.first_obstacle_position = True
        
        # powerups
        self.unfreeze = False

        # timers
        self.timer_1_seconds = 1
        self.timer_2_seconds = 1
        self.timer_3_miliseconds = 10
        self.timer_1_active = False
        self.timer_2_active = False
        self.timer_3_active = False

        ## Game stages / button actives
        self.button_mainmenu_active = 1
        self.button_start_active = 2
        self.button_leaderboard_active = 3
        self.button_back_active = 4 
        self.button_playagain_active = 5 
        self.death = 6
        self.button_exit_active = 7 
        self.option = self.button_mainmenu_active

        ## Other classes
        self.game_menu = Menu(self)
        self.end_screen = Endscreen(self)
        self.player = Player(self)
        self.rainbow_rect = Rainbow_rect(self)
        self.obstacles = []
        self.obstacles.append(Obstacles(self, self.player))
        self.powerups = Powerups(self)

        ## Sprites and groups
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.rainbow_rect_group = pygame.sprite.GroupSingle(self.rainbow_rect)
        self.obstacles_group = pygame.sprite.Group(self.obstacles[0])
        self.powerups_group = pygame.sprite.GroupSingle(self.powerups)

        ## Main game loop
        while True:
            self.tick()
            # print(self.screen_sizes[0]) ## DEBUG
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == timer_1 and self.timer_1_active:
                    if self.timer_1_seconds > 0:
                        self.timer_1_seconds -= 1
                if event.type == timer_2 and self.timer_2_active:
                    if self.timer_2_seconds > 0:
                        self.timer_2_seconds -= 1
                if event.type == timer_3:
                    self.timer_3_miliseconds += 1
            
            self.screen.fill(self.screen_color)
            
            ## Game stages
            match self.option:
                case self.button_mainmenu_active:
                    self.update_menu()
                    if self.option == self.button_start_active:
                        self.game_reset()

                case self.button_start_active:
                    self.powerups_timer()
                    self.update()
                    self.collisions()
            
                case self.button_leaderboard_active:
                    self.game_menu.leaderboard_show()

                case self.button_back_active:
                    self.option = self.button_mainmenu_active
                
                case self.button_playagain_active:
                    self.game_reset()
                    self.option = self.button_start_active

                case self.death:
                    self.screen_color = self.normal_color
                    self.last_score = self.score
                    
                    if not self.leaderboard_flag:
                        self.update_leaderboard()
                        self.leaderboard_flag = True

                    self.update_end_screen()

                case self.button_exit_active:
                    pygame.quit()
                    exit()

            pygame.display.update()

    def tick(self):
        self.clock.tick(self.fps)

    def collisions(self):
        ## PLAYER | RAINBOW_RECT
        if pygame.sprite.spritecollide(self.player_group.sprite, self.rainbow_rect_group, False, pygame.sprite.collide_mask) and not self.powerups.multiplier:
            self.score += 1
            while True:
                self.rainbow_rect.rect = self.rainbow_rect.surf.get_rect(topleft = (randint(30, self.screen_sizes[0][0]-30), randint(30, self.screen_sizes[0][1]-30)))
                if not pygame.sprite.spritecollide(self.rainbow_rect_group.sprite, self.obstacles_group, False, pygame.sprite.collide_mask) and not pygame.Rect.colliderect(self.rainbow_rect.rect, self.score_rect):
                    break
        elif pygame.sprite.spritecollide(self.player_group.sprite, self.rainbow_rect_group, False, pygame.sprite.collide_mask) and self.powerups.multiplier:
            self.score += 2
            while True:
                self.rainbow_rect.rect = self.rainbow_rect.surf.get_rect(topleft = (randint(30, self.screen_sizes[0][0]-30), randint(30, self.screen_sizes[0][1]-30)))
                if not pygame.sprite.spritecollide(self.rainbow_rect_group.sprite, self.obstacles_group, False, pygame.sprite.collide_mask) and not pygame.Rect.colliderect(self.rainbow_rect.rect, self.score_rect):
                    break

        ## PLAYER | POWERUPS
        if pygame.sprite.spritecollide(self.player_group.sprite, self.powerups_group, False,  pygame.sprite.collide_mask):
            shield = False
            multiplier = False
            freeze = False

            if self.powerups.type == 'shield':
                shield = True
            elif self.powerups.type == 'multiplier':
                multiplier = True
            elif self.powerups.type == 'freeze':
                freeze = True
            
            correct_icon = pygame.transform.scale(self.powerups.surf, (70, 70))
            self.powerups = Powerups(self)
            self.powerups_group.add(self.powerups)
            self.powerups.icon = correct_icon

            if shield:
                self.powerups.shield = True
            elif multiplier:
                self.powerups.multiplier = True
            elif freeze:
                self.powerups.freeze = True
                self.screen_color = self.freeze_color

            self.player.animation_started = True
            self.timer_2_seconds = 7
            self.timer_2_active = True
                
            self.powerups.show = False
            self.powerups.rect = self.powerups.surf.get_rect(center = (-1000, -1000))

        ## PLAYER | OBSTACLES
        if self.button_start_active:
            if pygame.sprite.spritecollide(self.player_group.sprite, self.obstacles_group, False, pygame.sprite.collide_mask) and not self.powerups.shield:
                self.option = self.death
            

    def update(self):
        pygame.mouse.set_visible(False)

        ## Player
        self.player.update()
        if self.player.animation_started:
            self.player.animation()

        ## Bonus
        self.rainbow_rect.update()

        ## Obstacles
        for i in range(0, len(self.obstacles)):
            self.obstacles[i].update()

        ## Adding one more obstacles every time when the player earn 5 points
        if self.score >= self.score_5:
            self.obstacles_counter += 1
            self.obstacles.append(Obstacles(self, self.player))
            self.obstacles_group.add(self.obstacles[self.obstacles_counter])
            self.score_5 += 5

        ## Score 
        self.display_score()

        ## Powerups
        self.powerups.update()

        # print(self.clock.get_fps()) ## DEBUG

    def update_menu(self):
        pygame.mouse.set_visible(True)

        while len(self.obstacles) < 25:
            self.obstacles.append(Obstacles(self, self.player))

        for i in range(0, len(self.obstacles)):
            self.obstacles[i].update()

        self.game_menu.update()

    def update_end_screen(self):
        pygame.mouse.set_visible(True)
        
        Endscreen(self).update()

    def display_score(self):
        self.score_text = self.font.render(f'Score: {self.score}', True, (0,0,0))
        self.score_rect = self.score_text.get_rect(center = (self.screen_x-125, 50))
        
        # # FPS DEBUG
        # self.fps_text = self.font.render(f"FPS: {self.clock.get_fps()}", True, (0,0,0))
        # self.fps_rect = self.fps_text.get_rect(center = (self.screen_x/2, 50))
        # self.screen.blit(self.fps_text, self.fps_rect)

        self.screen.blit(self.score_text, self.score_rect)

    def game_reset(self):
        self.obstacles_counter = 0
        self.first_obstacle_position = True
        self.score = 0
        self.score_5 = 5 
        self.leaderboard_flag = False
        self.timer_1_active = True
        self.timer_1_seconds = randint(2,3)
        self.timer_2_seconds = 0
        self.powerups.rect = self.powerups.surf.get_rect(center = (-1000, -1000))

        pygame.sprite.Group.empty(self.obstacles_group)
        self.obstacles.clear() 
        self.obstacles.append(Obstacles(self, self.player))
        self.obstacles_group.add(self.obstacles[self.obstacles_counter])

        pygame.sprite.GroupSingle.empty(self.powerups_group)
        self.powerups = Powerups(self)
        self.powerups_group = pygame.sprite.GroupSingle(self.powerups)

    def update_leaderboard(self):
        ranking = [self.last_score, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        with open("leaderboard.txt", "r") as file:
            for line in file.readlines():
                ranking.append(int(line.strip()))
        ranking.sort()
        ranking.reverse()
        while len(ranking) >= 11:
            ranking.pop()
        
        with open("leaderboard.txt") as file:
            pass

        with open("leaderboard.txt", "w") as file:
            for i in ranking:
                file.write(str(i)+'\n')

    def powerups_timer(self):
        ## Powerups active ends
        if self.timer_2_seconds == 0 and self.timer_2_active:
            image = pygame.image.load("images/Player/ball1.png").convert_alpha()
            self.player.surf = pygame.transform.scale(image, (60, 60))

            self.player.animation_started = False
            self.powerups.shield = False
            self.powerups.multiplier = False
            if self.powerups.freeze:
                self.unfreeze = True
            self.powerups.freeze = False

            self.timer_2_active = False
            self.timer_1_active = True
            self.timer_1_seconds = randint(15,20)

        ## New powerup on the screen
        if self.timer_1_seconds == 0 and self.timer_1_active:
            self.powerups.show = True
            self.timer_1_active = False
            self.powerups.rect = self.powerups.surf.get_rect(center = (randint(60, self.screen_sizes[0][0]-60), randint(60, self.screen_sizes[0][1]-60)))

        ## Freeze powerup mechanics
        if self.powerups.freeze:
            for i in range(0, len(self.obstacles)):
                self.obstacles_vel_storage.append([self.obstacles[i].vel, self.obstacles[i].vel_x, self.obstacles[i].vel_y])
                self.obstacles[i].vel = 0
                self.obstacles[i].vel_x = 0
                self.obstacles[i].vel_y = 0
        elif not self.powerups.freeze and self.unfreeze:
            self.unfreeze = False
            self.screen_color = self.normal_color
            for i in range(0, len(self.obstacles)):
                if self.obstacles_vel_storage[i][0] != 0:
                    self.obstacles[i].vel = self.obstacles_vel_storage[i][0]
                    self.obstacles[i].vel_x = self.obstacles_vel_storage[i][1]
                    self.obstacles[i].vel_y = self.obstacles_vel_storage[i][2]
                else:
                    self.obstacles[i].vel = randint(3,6)
                    self.obstacles[i].vel_x = choice([self.obstacles[i].vel, self.obstacles[i].vel*-1])
                    self.obstacles[i].vel_y = choice([self.obstacles[i].vel, self.obstacles[i].vel*-1])


## Debug functions
        
    def screen_resize(self):
        counter = 0
        for i in self.screen_sizes[0]:
            self.screen_sizes[0][counter] = int(i/1.5)
            # print(self.screen_sizes[0][counter]) ## DEBUG
            counter += 1

if __name__ == "__main__":
    Game()