"""
Для того, чтобы разобраться с pygame. Выводит табличку, в каждой ячейке можно менять цвета.
Смена цветов - по щелчку мышью. 
"""
import random
from pygame.color import THECOLORS


import pygame
import sys

pygame.init()

# грубо ширина и высота
win_width = 800
win_height = 800
distance = 1
len_cell = 30
font = pygame.font.SysFont('couriernew', round(len_cell * 0.4) )

# точно ширина и высота окна
count_columns = win_width // (len_cell + distance) 
count_lines = win_height // (len_cell + distance)
print("count cells: ", count_columns * count_lines)
new_width = (distance + len_cell) * count_columns + distance
new_height = (distance + len_cell) * count_lines + distance

screen = pygame.display.set_mode((new_width, new_height))



class Grid():
    def __init__(self, screen:pygame.Surface, count_columns:int, count_lines:int, len_cell:int, distance:int):
        self.screen = screen
        self.count_columns = count_columns
        self.count_lines = count_lines
        self.len_cell = len_cell
        self.distance = distance
        self.screen_width, self.screen_height = screen.get_size()
        self.cells = {}

    def create(self):
        for line in range(self.count_lines):
            for column in range(self.count_columns):
                x_cells = (self.len_cell + self.distance) * column + self.distance
                y_cells = (self.len_cell + self.distance) * line + self.distance
                pk = line * count_columns + column
                self.cells[pk] = Cell(pk=pk, grid=self, x_cells=x_cells, y_cells=y_cells, len_cell=self.len_cell, font=font)

    def change_color_cell(self, pk, new_color):
        """
        Изменяет цвет одной из ячеек
        """
        self.cells[pk].set_color_background(new_color)
    
    def random_change_color_cells(self):
        max_pk = self.count_lines * self.count_columns
        count_change_cells = random.randrange(0, max_pk)
        pk_change_cells = [random.randrange(0, max_pk) for i in range(0, count_change_cells)]
        list_colors = ["white", "gray", "green", "red", "yellow", "blue", "aqua", "purple", "teal"]
        for pk in pk_change_cells:
            self.change_color_cell(pk, THECOLORS[random.choice(list_colors)])



class Cell():
    def __init__(
            self, 
            pk:int,
            grid:Grid,
            x_cells:int,
            y_cells:int,
            len_cell:int,
            font:pygame.font.Font,
            color_background=THECOLORS["green"],
            color_text = THECOLORS["black"]
        ):
        self.pk = pk
        self.text = str(pk)
        self.grid = grid
        self.screen = grid.screen
        self.x_cells = x_cells
        self.y_cells = y_cells
        self.x_text_object = 0
        self.y_text_object = 0
        self.len_cell = len_cell
        self.font = font
        self.color_background = color_background
        self.color_text = color_text

        self.cell = pygame.draw.rect(self.screen, self.color_background, (self.x_cells, self.y_cells, self.len_cell, self.len_cell), width=0)
        self.text_object = font.render(str(self.text), True, self.color_text)
        width_text_object, height_text_object = self.text_object.get_size()
        self.x_text_object = self.x_cells + (self.len_cell - width_text_object) // 2
        self.y_text_object = self.y_cells + (self.len_cell - height_text_object) // 2
        screen.blit(self.text_object, (self.x_text_object, self.y_text_object))

    def set_color_background(self, new_color):
        self.cell = pygame.draw.rect(self.screen, new_color, (self.x_cells, self.y_cells, self.len_cell, self.len_cell), width=0)
        screen.blit(self.text_object, (self.x_text_object, self.y_text_object))





screen.fill(THECOLORS['black'])
grid = Grid(screen=screen, count_columns=count_columns, count_lines=count_lines, len_cell=len_cell, distance=distance)
grid.create()


while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                grid.random_change_color_cells()
        pygame.display.flip()
    except:
        pygame.quit()
        exit()
