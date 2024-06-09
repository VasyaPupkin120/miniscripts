from pygame.color import THECOLORS

import pygame
import sys

pygame.init()
win_width = 1450
win_height = 1000

screen = pygame.display.set_mode((win_width, win_height))
screen.fill(THECOLORS['green'])

flag_widht = 1350
flag_height = 900
flag_x = (win_width - flag_widht) // 2
flag_y = (win_height - flag_height) // 2
flag = pygame.draw.rect(screen, THECOLORS['white'], (flag_x, flag_y, flag_widht, flag_height), width=0)

width_circles = 20
radius_circles = (flag_height // 3) // 2
half_radius = radius_circles // 2
delta_x = radius_circles // 5

circles = {}
circles["blue"] = {"color": THECOLORS["blue"], "center_x": (flag_widht // 2) - 2 * radius_circles - delta_x, "center_y": (flag_height // 2) - half_radius}
circles["black"] = {"color": THECOLORS["black"], "center_x": flag_widht // 2, "center_y": (flag_height // 2) - half_radius}
circles["red"] = {"color": THECOLORS["red"], "center_x": (flag_widht // 2) + 2 * radius_circles + delta_x, "center_y": (flag_height // 2) - half_radius}
circles["yellow"] = {"color": THECOLORS["yellow"], "center_x": (flag_widht // 2) - radius_circles - delta_x // 2, "center_y": (flag_height // 2) + half_radius}
circles["green"] = {"color": THECOLORS["green"], "center_x": (flag_widht // 2) + radius_circles + delta_x // 2, "center_y": (flag_height // 2) + half_radius}

for circle in circles.values():
    pygame.draw.circle(screen, circle["color"], (circle["center_x"], circle["center_y"]), radius_circles, width_circles)

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        pygame.display.flip()
    except:
        pygame.quit()
        exit()
