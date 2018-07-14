from random import randint, choice
import tkinter as tk

from positioning import Position2D, Direction, DIRECTIONS2D


class Map(tk.Tk):
    def __init__(self, x_max: int, y_max: int, organism_nbr: int):
        super().__init__()
        self.x_max = x_max
        self.y_max = y_max
        self.organisms = {
            Organism(self, Position2D((randint(0, x_max), randint(0, y_max)))) for _ in range(organism_nbr)
        }


class Organism:
    def __init__(self, map_: Map, position: Position2D):
        self.size = randint(1, 100)
        self.map = map_
        self.position = position

    def move(self, direction: Direction):
        self.position += direction

    def choose_direction(self):
        return choice(
            [
                direction
                for direction in DIRECTIONS2D
                if (self.position + direction).belongs_to(self.map.x_max, self.map.y_max)
            ]
        )


def test():
    m = Map(4, 3, 15)
    print(vars(m))


if __name__ == "__main__":
    test()
