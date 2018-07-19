from random import choices, randint, choice

from Py2Dmap import BaseCell, Pawn, Direction, Map


class Organism(Pawn):
    def __init__(self):
        super().__init__()
        self._color = "#" + "".join(choices("0123456789ABC", k=6))
        self.speed = randint(1, 5)
        self.mass = 5 - self.speed

    @property
    def color(self):
        return self._color

    def run(self):
        for _ in range(self.speed):

            next_cell = self.cell.get_cell_by_direction(Direction((randint(-1, 1), randint(-1, 1))), None)
            if next_cell is not None:
                for pawn in next_cell._stack:
                    if pawn.mass > self.mass:
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
                    self.cell.mother.remove_pawn(dead)
                    if dead is self:
                        return


class Cell(BaseCell):
    @property
    def color(self):
        if not self._stack:
            return "#EEEEEE"
        return self._stack[-1].color


m = Map(70, 70, Cell)
for i in range(40):
    m.add_pawn(Organism(), (randint(0, 49), randint(0, 49)))
m.mainloop()
