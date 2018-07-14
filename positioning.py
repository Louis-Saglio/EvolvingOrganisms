from typing import Tuple, Union


class Direction:
    def __init__(self, name: str, vector: Tuple[Union[int, float], Union[int, float]]):
        self.name = name
        self.vector = vector


DIRECTIONS2D = UP, DOWN, LEFT, RIGHT = (
    Direction("UP", (0, 1)),
    Direction("DOWN", (0, -1)),
    Direction("LEFT", (-1, 0)),
    Direction("RIGHT", (1, 0)),
)


class Position2D:
    def __init__(self, position: Tuple[Union[int, float], Union[int, float]]):
        self._position = list(position)

    def __add__(self, direction: Direction):
        return Position2D((self._position[0] + direction.vector[0], self._position[1] + direction.vector[1]))

    def belongs_to(self, x_max, y_max):
        return self._position[0] <= x_max and self._position[1] <= y_max

    def move(self, direction: Direction):
        self._position = self + direction


def test():
    p = Position2D((5, 8))
    p.move(UP)
    print(vars(p))


if __name__ == "__main__":
    test()
