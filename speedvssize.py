import random

from positioning import Position2D, Direction, DIRECTIONS2D


class Map:
    def __init__(self, x_max: int, y_max: int):
        self.x_max = x_max
        self.y_max = y_max


class Organism:
    def __init__(self, map_, position: Position2D):
        self.size = random.randint(1, 100)
        self.map = map_
        self.position = position

    def move(self, direction: Direction):
        self.position += direction

    def choose_direction(self):
        return random.choice(
            [
                direction
                for direction in DIRECTIONS2D
                if (self.position + direction).belongs_to(self.map.x_max, self.map.y_max)
            ]
        )


def test():
    m = Map(4, 3)
    o = Organism(m, Position2D((4, 3)))
    print(o.position.belongs_to(m.x_max, m.y_max))
    print(o.choose_direction().__dict__)


if __name__ == "__main__":
    test()
