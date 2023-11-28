from Animations import *

tile_SIZE = 50
width_tilemap = 82
height_tilemap = 52


class Player:
    def __init__(self, surface):
        pygame.font.init()
        self.speed = 5
        self.direction = 0
        self.player_anim = anim_player
        self.player_anim_left = anim_player_reverse
        self.anim_count = 0
        self.attack_image = anim_attack
        self.attack_image_left = anim_attack_reverse
        self.anim_count_attack = 0
        self.image = self.player_anim[0]
        self.surface = surface
        self.surface_rect = self.surface.get_rect()
        self.player_center = self.image.get_rect()
        self.player_center.centerx, self.player_center.centery = ((tile_SIZE * width_tilemap) / 2), ((tile_SIZE * height_tilemap) / 2)
        self.x = self.player_center.centerx
        self.y = self.player_center.centery
        self.vector = [0, 0]
        self.player_health = 100
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)


    def spawn_player(self):
        if self.anim_count == 9:
            self.anim_count = 0
        else:
            self.anim_count += 1
        kep = pygame.key.get_pressed()
        current_image = [self.player_anim[self.anim_count], self.player_anim_left[self.anim_count]]
        if kep[pygame.K_d]:
            self.direction = 0
        if kep[pygame.K_a]:
            self.direction = 1
        self.surface.blit(current_image[self.direction], self.player_center)

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and self.y < 1990:
            self.y += self.speed
            self.vector[1] = self.y
        if keys[pygame.K_w] and self.y > 540:
            self.y -= self.speed
            self.vector[1] = self.y
        if keys[pygame.K_d] and self.x < 3140:
            self.x += self.speed
            self.vector[0] = self.x
        if keys[pygame.K_a] and self.x > 960:
            self.x -= self.speed
            self.vector[0] = self.x


    def attack_player(self, enemies):
        if self.anim_count_attack == 5:
            self.anim_count_attack = 0
        else:
            self.anim_count_attack += 1
        keys = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if keys[0]:
            if pos[0] < self.player_center.centerx - 60:
                pos = (self.player_center.centerx - 60, pos[1])
            elif pos[0] > self.player_center.centerx + 60:
                pos = (self.player_center.centerx + 60, pos[1])
            if pos[1] < self.player_center.centery - 72 - 80:
                pos = (pos[0], self.player_center.centery - 72 - 80)
            elif pos[1] > self.player_center.centery + 80:
                pos = (pos[0], self.player_center.centery + 80)

            if pos[0] < self.player_center.centerx:
                pos = (pos[0] - 51, pos[1])
                self.surface.blit(self.attack_image_left[self.anim_count_attack], (pos[0], pos[1]))
            else:
                self.surface.blit(self.attack_image[self.anim_count_attack], (pos[0], pos[1]))



            for enemy in enemies:
                if enemy.enemy.colliderect(pygame.Rect(pos[0], pos[1], 51, 80)):
                    enemy.enemy_health -= 10
                    # pygame.draw.rect(self.surface, (225, 0, 0),(pos[0], pos[1], 51, 80), 3)
                if enemy.enemy_health <= 0:
                    self.score += 1
                    enemies.remove(enemy)

    def draw_player_health_bar(self):
        health_bar_width = int(self.player_health)
        pygame.draw.rect(self.surface, (0, 225, 0), (self.player_center.x, self.player_center.y-25, health_bar_width, 20))

    def draw_score(self):
        text_score = self.font.render(f"SCORE: {self.score}/25", False, (255, 0, 0))
        self.surface.blit(text_score, (2000, 760))


    def update_player(self):
        self.spawn_player()
        self.move_player()
        self.draw_player_health_bar()
        self.draw_score()


class Enemy(Player):

    def __init__(self, surface, x, y):
        super().__init__(surface)
        self.surface = surface
        self.enemy_anim = anim_enemy
        self.enemy_anim_left = anim_enemy_reverse
        self.anim_count = 0
        self.image_enemy = self.enemy_anim[0]
        self.enemy = self.image_enemy.get_rect()
        self.enemy.centerx, self.enemy.centery = x, y
        self.image_dir = 0
        self.enemy_speed = 2.5
        self.count_enemy = 10
        self.enemy_health = 100


    def move_enemy(self, player):
        keys = pygame.key.get_pressed()
        if self.enemy.colliderect(pygame.Rect(player.player_center.x, player.player_center.y - 5, 101, 144)):
            player.player_health -= 1
        # if player.player_health <= 0:
        #     self.surface.blit(self.died_screen, (1090, 760))
        #     self.died_music.play()
        if keys[pygame.K_s]:
            self.enemy.centery -= self.enemy_speed
        if keys[pygame.K_w]:
            self.enemy.centery += self.enemy_speed
        if keys[pygame.K_d]:
            self.enemy.centerx -= self.enemy_speed
        if keys[pygame.K_a]:
            self.enemy.centerx += self.enemy_speed

        # pygame.draw.rect(self.surface, (225, 0, 0), (self.player_center.x, self.player_center.y-5, 101, 144), 5)


    def move_into_player(self):
        if self.enemy.centerx > self.player_center.centerx:
            self.enemy.centerx -= self.enemy_speed
        if self.enemy.centerx < self.player_center.centerx:
            self.enemy.centerx += self.enemy_speed
        if self.enemy.centery > self.player_center.centery:
            self.enemy.centery -= self.enemy_speed
        if self.enemy.centery < self.player_center.centery:
            self.enemy.centery += self.enemy_speed

    def draw_enemy(self):
        if self.anim_count == 11:
            self.anim_count = 0
        else:
            self.anim_count += 1
        current_image = [self.enemy_anim[self.anim_count], self.enemy_anim_left[self.anim_count]]
        if self.enemy.centerx > self.player_center.centerx:
            self.image_dir = 1
        if self.enemy.centerx < self.player_center.centerx:
            self.image_dir = 0
        self.surface.blit(current_image[self.image_dir], self.enemy)
        self.draw_enemy_health_bar()


    def spawn_enemy(self):
        self.draw_enemy()

    def enemy_update(self):
        self.spawn_enemy()
        self.move_into_player()


    def draw_enemy_health_bar(self):
        health_bar_width = int(self.enemy_health / 100 * self.enemy.width)
        pygame.draw.rect(self.surface, (225, 0, 0), (self.enemy.x, self.enemy.y - 10, health_bar_width, 5))

