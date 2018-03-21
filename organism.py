import random


class Direction:
    VALUES = H, B, G, D = "HBGD"


class Organism:

    def __init__(self, x: float=None, y: float=None):
        self.x = x if x is not None else random.random()
        self.y = y if y is not None else random.random()
        self.gui_manager = None
        self.speed = random.random() / 10
        self.direction = random.choice(Direction.VALUES)

    def move(self):
        if self.direction == Direction.H:
            self.y += self.speed
        elif self.direction == Direction.B:
            self.y -= self.speed
        elif self.direction == Direction.D:
            self.x += self.speed
        elif self.direction == Direction.G:
            self.x -= self.speed
        if int(self.x) not in range(0, 1) or int(self.y) not in range(0, 1):
            raise ValueError("Invalid position")


def main():
    o = Organism()
    print(vars(o))
    o.move()
    print(vars(o))


if __name__ == '__main__':
    main()
