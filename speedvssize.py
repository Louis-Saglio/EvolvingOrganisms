from random import choices, randint

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

            self.move(Direction((randint(-1, 1), randint(-1, 1))))

            maxi = None
            for pawn in self.cell._stack:
                if isinstance(pawn, Organism):
                    if maxi is None:
                        maxi = pawn.mass
                    if pawn.mass < maxi:
                        self.cell.mother.remove_pawn(pawn)
                        return


class Cell(BaseCell):
    @property
    def color(self):
        if not self._stack:
            return "#EEEEEE"
        return self._stack[-1].color

    # def put(self, pawn: "Pawn"):
    #     super().put(pawn)
    #     maxi = None
    #     for pawn in self._stack:
    #         if isinstance(pawn, Organism):
    #             if maxi is None:
    #                 maxi = pawn.mass
    #             if pawn.mass < maxi:
    #                 self.mother.remove_pawn(pawn)
    #                 break


m = Map(70, 70, Cell)
for i in range(40):
    m.add_pawn(Organism(), (randint(0, 49), randint(0, 49)))
m.mainloop()
