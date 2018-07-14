from typing import Tuple, Union


class Direction:
    def __init__(self, name: str, vector: Tuple[Union[int, float], Union[int, float]]):
        self.name = name
        self.vector = vector


UP, DOWN, LEFT, RIGHT = (
    Direction("UP", (0, 1)),
    Direction("DOWN", (0, -1)),
    Direction("LEFT", (-1, 0)),
    Direction("RIGHT", (1, 0)),
)


class Position2D:
    def __init__(self, position: Tuple[Union[int, float], Union[int, float]]):
        self.position = list(position)

    def __add__(self, direction: Direction):
        self.position[0] += direction.vector[0]
        self.position[1] += direction.vector[1]

    def move(self, direction: Direction):
        self + direction


def test():
    p = Position2D((5, 8))
    p.move(UP)
    print(vars(p))


if __name__ == "__main__":
    test()
