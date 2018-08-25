from pprint import pprint
from random import randint, choice, choices
from typing import Union

from Py2Dmap import BaseCell, Pawn, Direction, Map

organism_counter = {}
food_counter = {}


class Organism(Pawn):
    def __init__(self, color=None, speed=None):
        super().__init__()
        self._color = color or "#" + "".join(choices("56789AB", k=6))
        self.speed = speed or randint(1, 20)
        self.mass = -self.speed
        self.energy = 70
        self.age = 0
        if self.speed in organism_counter:
            organism_counter[self.speed] += 1
        else:
            organism_counter[self.speed] = 1

    def get_clone(self) -> "Organism":
        speed = self.speed
        color = self.color
        if randint(0, 50) == 0:
            speed += choice((-1, 1))
            color = None
        return Organism(color, speed)

    @property
    def color(self):
        return self._color

    def eat(self, other: Union["Organism", "Food"]):
        other.cell.mother.remove_pawn(other)
        self.energy += other.energy
        if self.energy > 200:
            self.energy = 200

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
                    self.cell.mother.add_pawn(self.get_clone(), birth_cell.position._position)

            next_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
            if next_cell is not None:
                # for pawn in next_cell._stack:
                # if isinstance(pawn, Organism) and pawn.mass > self.mass:
                #     break
                # else:
                self.go_to(next_cell)

            for pawn in self.cell._stack:
                if pawn is not self and isinstance(pawn, Organism):
                    if self.mass < pawn.mass:
                        dead = self
                    elif self.mass > pawn.mass:
                        dead = pawn
                    elif self.color != pawn.color:
                        dead = choice((self, pawn))
                    else:
                        dead = None
                        # dead = choice((self, pawn))
                    if dead is self:
                        # noinspection PyTypeChecker
                        pawn.eat(self)
                        return
                    elif dead is not None:
                        self.eat(pawn)
                elif isinstance(pawn, Food):
                    self.eat(pawn)


class Food(Pawn):
    def __init__(self, energy=None, color=None):
        super().__init__()
        self.energy = energy or 50
        self.age = 0
        self._color = color or "#" + "".join(choices("01234", k=6))
        if self.energy in food_counter:
            food_counter[self.energy] += 1
        else:
            food_counter[self.energy] = 1

    @property
    def color(self):
        return self._color

    def run(self):
        self.age += 1
        if self.age % 30 == 0:
            next_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
            if next_cell is not None and not next_cell._stack:
                if randint(0, 99) == 0:
                    energy = self.energy + choice(tuple(range(-10, 10)))
                    color = "#" + "".join(choices("01234", k=6))
                else:
                    energy = self.energy
                    color = self.color
                self.cell.mother.add_pawn(Food(energy, color), next_cell.position._position)


class Cell(BaseCell):
    @property
    def color(self):
        if not self._stack:
            return "#EEEEEE"
        return self._stack[-1].color


m = Map(100, 100, Cell)
# m = Map(100, 170, Cell)
for i in range(70):
    m.add_pawn(Organism(color="#885599", speed=5), (randint(0, m.width-1), randint(0, m.height-1)))
    m.add_pawn(Food(energy=randint(10, 75)), (randint(0, m.width-1), randint(0, m.height-1)))
generation_nbr, nbr_remaining = m.mainloop()
print(generation_nbr, nbr_remaining)

pprint(organism_counter)
pprint(food_counter)
