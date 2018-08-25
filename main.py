from random import randint
from typing import Set, Tuple, List, Union


class Organism:
    def __init__(self):
        self.genome = {
            "similarity_factor": randint(0, 9),
            "up_factor": randint(0, 9),
            "down_factor": randint(0, 9),
            "left_factor": randint(0, 9),
            "right_factor": randint(0, 9),
            "1_distance_factor": randint(0, 9),
            "2_distance_factor": randint(0, 9),
        }

    def get_similarity_with(self, other: "Organism") -> int:
        raise NotImplementedError

    def analyse_cell_for_dir(self, other: "Organism", direction: str, distance: int) -> int:
        return (
            self.get_similarity_with(other)
            * self.genome["similarity_factor"]
            * self.genome[direction + "_factor"]
            * self.genome[str(distance) + "_distance_factor"]
        )

    def choose_direction(self, data: Set[Tuple["Organism", str, int]]):
        next_directions = {}
        for datum in data:
            next_directions[datum[1]] = self.analyse_cell_for_dir(*datum)
        print(next_directions)
        return max(next_directions, key=lambda x: next_directions[x])


class Engine:
    def __init__(self, nbr: int = 0):
        self.organisms: List[Tuple[Tuple[int, int], Organism]] = [
            ((randint(0, 99), randint(0, 99)), Organism()) for _ in range(nbr)
        ]

    def get_organism_by_position(self, x: int, y: int) -> Union[None, Organism]:
        for organism in self.organisms:
            if organism[0] == (x, y):
                return organism[1]

    def get_vision_for_cell(self, x: int, y: int):
        return {
            (self.get_organism_by_position(x, y + 1), "up", 1),
            (self.get_organism_by_position(x, y + 2), "up", 2),
            (self.get_organism_by_position(x, y - 1), "down", 1),
            (self.get_organism_by_position(x, y - 2), "down", 2),
            (self.get_organism_by_position(x + 1, y), "right", 1),
            (self.get_organism_by_position(x + 2, y), "right", 1),
            (self.get_organism_by_position(x - 1, y), "left", 1),
            (self.get_organism_by_position(x - 2, y), "left", 2),
        }

    def move_organisms(self):
        for organism in self.organisms:
            print(organism[0])
            organism[1].choose_direction(self.get_vision_for_cell(*organism[0]))


def main():
    # o = Organism()
    # print(o.choose_dir({(o, "up", 1), (o, "down", 2), (o, "left", 1), (o, "right", 1)}))
    Engine(10).move_organisms()


if __name__ == "__main__":
    main()
