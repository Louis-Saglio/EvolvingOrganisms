from random import choices, randint

from Py2Dmap import BaseCell, Pawn, Direction, Map, BadPositionException


class Organism(Pawn):
    def __init__(self):
        super().__init__()
        self._color = "#" + "".join(choices("0123456789ABCDEF", k=6))
        self.speed = randint(1, 5)
        self.mass = 5 - self.speed

    @property
    def color(self):
        return self._color

    def run(self):
        for _ in range(self.speed):
            try:
                if self._cell:
                    self.move(Direction((randint(-1, 1), randint(-1, 1))))
            except BadPositionException:
                pass


class Cell(BaseCell):
    @property
    def color(self):
        if not self._stack:
            return "#EEEEEE"
        return self._stack[-1].color

    def put(self, pawn: "Pawn"):
        super().put(pawn)
        maxi = None
        for pawn in self._stack:
            if isinstance(pawn, Organism):
                if maxi is None:
                    maxi = pawn.mass
                if pawn.mass < maxi:
                    self.mother.remove_pawn(pawn)
                    break


m = Map(50, 50, Cell)
for i in range(20):
    m.add_pawn(Organism(), (randint(0, 49), randint(0, 49)))
m.mainloop()
