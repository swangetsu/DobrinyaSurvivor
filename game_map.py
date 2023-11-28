import pygame as pg
from random import randint

tile_SIZE = 50
width_tilemap = 82
height_tilemap = 52
map_surface = pg.surface.Surface((tile_SIZE*width_tilemap, tile_SIZE*height_tilemap))

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, group, num_of_tile):
        super().__init__(group)
        self.image = pg.image.load(fr'./sprites/tiles_map/{num_of_tile}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class GameMap:
    def __init__(self):

        self.tiles_group = pg.sprite.Group()
        self.map_create()

    def map_create(self):
        Generated_Map = [[0 for _ in range(width_tilemap)] for _ in range(height_tilemap)]
        for row in range(height_tilemap):
            for col in range(width_tilemap):
                Generated_Map[row][col] = randint(1, 7)

        for row_index, row in enumerate(Generated_Map):
            for col_index, col in enumerate(row):
                x = col_index * tile_SIZE
                y = row_index * tile_SIZE
                tile_num = Generated_Map[row_index][col_index]
                Tile((x, y), self.tiles_group, tile_num)
        Tile((0, 0), self.tiles_group, 8)
        Tile((3140, 0), self.tiles_group, 9)
        Tile((960, 0), self.tiles_group, 10)
        Tile((960, 2060), self.tiles_group, 10)


    def run(self):
        self.tiles_group.draw(map_surface)




