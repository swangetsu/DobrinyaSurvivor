import sys
import pygame
from game_map import *
from Player import Player, Enemy
import random


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = tile_SIZE*width_tilemap
        self.HEIGHT = tile_SIZE*height_tilemap
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), vsync=30)
        pygame.display.set_caption('Dobrinya_Survivor')
        self.clock = pygame.time.Clock()
        self.level = GameMap()
        self.player = Player(self.screen)
        self.enemy_list = [Enemy(self.screen, random.randint(0, 4600), random.randint(0, 540)),
                           Enemy(self.screen, random.randint(0, 4600), random.randint(2060, 2600)),
                           Enemy(self.screen, random.randint(0, 960), random.randint(540, 2060)),
                           Enemy(self.screen, random.randint(3140, 4600), random.randint(540, 2060)),
                           Enemy(self.screen, random.randint(0, 4600), random.randint(0, 540)),
                           Enemy(self.screen, random.randint(0, 4600), random.randint(2060, 2600)),
                           Enemy(self.screen, random.randint(0, 960), random.randint(540, 2060)),
                           Enemy(self.screen, random.randint(3140, 4600), random.randint(540, 2060)),
                           Enemy(self.screen, random.randint(0, 4600), random.randint(0, 540)),
                           Enemy(self.screen, random.randint(0, 4600), random.randint(2060, 2600))]
        self.player_centerx = None
        self.player_centery = None
        self.check_menu = False
        self.check_death = False
        self.check_win = False
        self.menu = pygame.image.load('sprites/main_menu.png').convert_alpha()
        self.main_music = pygame.mixer.Sound(
            'soundtracks/Mick_Gordon_-_The_Only_Thing_They_Fear_Is_You_DOOM_Eternal_OST_69283083.mp3')
        self.menu_music = pygame.mixer.Sound('soundtracks/Hirasawa_Susumu_-_Guts_Theme_Berserk_66802816.mp3')
        self.menu_music.play()
        self.died_music = pygame.mixer.Sound('soundtracks/you_died.mp3')
        self.died_screen = pygame.image.load('sprites/you_died.png')
        self.won_music = pygame.mixer.Sound('soundtracks/you_survived.mp3')
        self.win_screen = pygame.image.load('sprites/you_survived.png')


    def check_enemy_collisions(self):
        speed = 2.5
        for i in range(len(self.enemy_list)):
            for j in range(i + 1, len(self.enemy_list)):
                enemy1 = self.enemy_list[i]
                enemy2 = self.enemy_list[j]

                if enemy1.enemy.colliderect(enemy2.enemy):
                    if enemy1.enemy.centerx < enemy2.enemy.centerx:
                        enemy1.enemy.centerx -= speed
                        enemy2.enemy.centerx += speed
                    else:
                        enemy1.enemy.centerx += speed
                        enemy2.enemy.centerx -= speed

                    if enemy1.enemy.centery < enemy2.enemy.centery:
                        enemy1.enemy.centery -= speed
                        enemy2.enemy.centery += speed
                    else:
                        enemy1.enemy.centery += speed
                        enemy2.enemy.centery -= speed

    def update_list_enemy(self):
        if len(self.enemy_list) < 10:
            a = random.randint(1, 4)
            if a == 1:
                self.enemy_list.append(Enemy(self.screen, random.randint(0, 4600), random.randint(0, 540)))
            if a == 2:
                self.enemy_list.append(Enemy(self.screen, random.randint(0, 4600), random.randint(2060, 2600)))
            if a == 3:
                self.enemy_list.append(Enemy(self.screen, random.randint(0, 960), random.randint(540, 2060)))
            if a == 4:
                self.enemy_list.append(Enemy(self.screen, random.randint(3140, 4600), random.randint(540, 2060)))

    def main_menu(self):
        self.screen.blit(self.menu, (1090, 760))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.menu_music.stop()
            self.main_music.play()
            self.check_menu = True
        self.exit_to_desktop()

    def dead(self):
        if not self.check_death:
            self.main_music.stop()
            self.died_music.play()
            self.check_death = True
        self.screen.blit(self.died_screen, (1090, 760))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            start()
        self.exit_to_desktop()

    def win(self):
        if not self.check_win:
            self.main_music.stop()
            self.won_music.play()
            self.check_win = True
        self.screen.blit(self.win_screen, (1090, 760))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            start()
        self.exit_to_desktop()

    def exit_to_desktop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

    def run(self):
        while True:
            self.check_enemy_collisions()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if not self.check_menu:
                self.main_menu()
            else:
                if self.player.player_health > 0:
                    if self.player.score < 25:
                        self.level.run()
                        self.screen.blit(map_surface, (self.WIDTH/2 - self.player.x, self.HEIGHT/2 - self.player.y))
                        self.player.update_player()
                        for enm in self.enemy_list:
                            if self.player.x != 960 and self.player.x != 3140 and self.player.y != 1990 and self.player.y != 540:
                                enm.move_enemy(self.player)
                            enm.enemy_update()
                        self.player.attack_player(self.enemy_list)
                        self.update_list_enemy()
                        self.exit_to_desktop()
                    else:
                        self.win()
                else:
                    self.dead()

            pygame.display.update()
            self.clock.tick(30)

def start():
    game = Game()
    game.run()

if __name__ == '__main__':
    start()