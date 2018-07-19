from random import choices, randint, choice
from typing import Union

from Py2Dmap import BaseCell, Pawn, Direction, Map


class Organism(Pawn):
    def __init__(self, color=None, speed=None):
        super().__init__()
        self._color = color or "#" + "".join(choices("0123456789ABC", k=6))
        self.speed = speed or randint(1, 20)
        self.mass = 20 - self.speed
        self.energy = 70
        self.age = 0

    def get_clone(self) -> "Organism":
        speed = self.speed
        color = self.color
        if randint(0, 99) == 0:
            speed += choice((-1, 1))
            color = None
        return Organism(color, speed)

    @property
    def color(self):
        return self._color

    def eat(self, other: Union["Organism", "Food"]):
        other.cell.mother.remove_pawn(other)
        self.energy += other.energy

    def run(self):
        if self.energy == 0:
            self.cell.mother.remove_pawn(self)
            return
        self.energy -= 1
        for _ in range(self.speed):
            self.age += 1
            if self.age % 1000 == 0:
                birth_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
                if birth_cell is not None:
                    self.cell.mother.add_pawn(
                        self.get_clone(), birth_cell.position._position
                    )

            next_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
            if next_cell is not None:
                for pawn in next_cell._stack:
                    if isinstance(pawn, Organism) and pawn.mass > self.mass:
                        break
                else:
                    self.go_to(next_cell)

            for pawn in self.cell._stack:
                if pawn is not self and isinstance(pawn, Organism):
                    if self.mass < pawn.mass:
                        dead = self
                    elif self.mass > pawn.mass:
                        dead = pawn
                    else:
                        dead = choice((self, pawn))
                    if dead is self:
                        # noinspection PyTypeChecker
                        pawn.eat(self)
                        return
                    else:
                        self.eat(pawn)
                elif isinstance(pawn, Food):
                    self.eat(pawn)


class Food(Pawn):
    def __init__(self):
        super().__init__()
        self.energy = 30

    @property
    def color(self):
        return "#000000"

    def run(self):
        self.energy += 1
        if self.energy % 60 == 0:
            next_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
            if next_cell is not None and not [pawn for pawn in next_cell._stack if isinstance(pawn, Food)]:
                self.cell.mother.add_pawn(Food(), next_cell.position._position)


class Cell(BaseCell):
    @property
    def color(self):
        if not self._stack:
            return "#EEEEEE"
        return self._stack[-1].color


m = Map(70, 70, Cell)
for i in range(40):
    m.add_pawn(Organism(), (randint(0, 69), randint(0, 69)))
    m.add_pawn(Food(), (randint(0, 69), randint(0, 69)))
pawns = m.mainloop()
for pawn in pawns:
    if isinstance(pawn, Organism):
        print(pawn.mass)
