import random
import time

import pygame

import organism
import gui
from organism import Direction

o = organism.Organism()

screen = pygame.display.set_mode((500, 500))

o.gui_manager = gui.PygameOrganism(o, screen)
o.gui_manager.draw()

while True:
    try:
        o.move()
        if random.randint(0, 9) == 0:
            raise ValueError
    except ValueError:
        o.direction = random.choice(Direction.VALUES)
    screen.fill((0, 0, 0))
    o.gui_manager.draw()
    time.sleep(0.1)
    pygame.display.flip()
