import pygame

anim_player = [pygame.image.load('sprites/player_anim/1.png'),
               pygame.image.load('sprites/player_anim/1.png'),
               pygame.image.load('sprites/player_anim/2.png'),
               pygame.image.load('sprites/player_anim/2.png'),
               pygame.image.load('sprites/player_anim/3.png'),
               pygame.image.load('sprites/player_anim/3.png'),
               pygame.image.load('sprites/player_anim/4.png'),
               pygame.image.load('sprites/player_anim/4.png'),
               pygame.image.load('sprites/player_anim/5.png'),
               pygame.image.load('sprites/player_anim/5.png')]

anim_player_reverse = [pygame.transform.flip(anim_player[0], True, False),
                       pygame.transform.flip(anim_player[1], True, False),
                       pygame.transform.flip(anim_player[2], True, False),
                       pygame.transform.flip(anim_player[3], True, False),
                       pygame.transform.flip(anim_player[4], True, False),
                       pygame.transform.flip(anim_player[5], True, False),
                       pygame.transform.flip(anim_player[6], True, False),
                       pygame.transform.flip(anim_player[7], True, False),
                       pygame.transform.flip(anim_player[8], True, False),
                       pygame.transform.flip(anim_player[9], True, False)]


anim_attack = [pygame.image.load('sprites/attack_anim/1.png'),
               pygame.image.load('sprites/attack_anim/2.png'),
               pygame.image.load('sprites/attack_anim/3.png'),
               pygame.image.load('sprites/attack_anim/4.png'),
               pygame.image.load('sprites/attack_anim/5.png'),
               pygame.image.load('sprites/attack_anim/6.png')]

anim_attack_reverse = [pygame.transform.flip(anim_attack[0], True, False),
                       pygame.transform.flip(anim_attack[1], True, False),
                       pygame.transform.flip(anim_attack[2], True, False),
                       pygame.transform.flip(anim_attack[3], True, False),
                       pygame.transform.flip(anim_attack[4], True, False),
                       pygame.transform.flip(anim_attack[5], True, False)]


anim_enemy = [pygame.image.load('sprites/wolf_anim/1.png'),
              pygame.image.load('sprites/wolf_anim/1.png'),
              pygame.image.load('sprites/wolf_anim/1.png'),
              pygame.image.load('sprites/wolf_anim/2.png'),
              pygame.image.load('sprites/wolf_anim/2.png'),
              pygame.image.load('sprites/wolf_anim/2.png'),
              pygame.image.load('sprites/wolf_anim/3.png'),
              pygame.image.load('sprites/wolf_anim/3.png'),
              pygame.image.load('sprites/wolf_anim/3.png'),
              pygame.image.load('sprites/wolf_anim/4.png'),
              pygame.image.load('sprites/wolf_anim/4.png'),
              pygame.image.load('sprites/wolf_anim/4.png')]

anim_enemy_reverse = [pygame.transform.flip(anim_enemy[0], True, False),
                      pygame.transform.flip(anim_enemy[1], True, False),
                      pygame.transform.flip(anim_enemy[2], True, False),
                      pygame.transform.flip(anim_enemy[3], True, False),
                      pygame.transform.flip(anim_enemy[4], True, False),
                      pygame.transform.flip(anim_enemy[5], True, False),
                      pygame.transform.flip(anim_enemy[6], True, False),
                      pygame.transform.flip(anim_enemy[7], True, False),
                      pygame.transform.flip(anim_enemy[8], True, False),
                      pygame.transform.flip(anim_enemy[9], True, False),
                      pygame.transform.flip(anim_enemy[10], True, False),
                      pygame.transform.flip(anim_enemy[11], True, False)]