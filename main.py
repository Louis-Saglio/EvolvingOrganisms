from typing import Set, Tuple


class Organism:
    def __init__(self):
        self.genome = {
            "similarity_factor": 5,
            "up_factor": 2,
            "down_factor": 2,
            "left_factor": 2,
            "right_factor": 2,
            "1_distance_factor": 1,
            "2_distance_factor": 1,
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

    def choose_dir(self, data: Set[Tuple["Organism", str, int]]):
        next_directions = {}
        for datum in data:
            next_directions[datum[1]] = self.analyse_cell_for_dir(*datum)
        print(next_directions)
        return max(next_directions, key=lambda x: next_directions[x])


def main():
    o = Organism()
    print(o.choose_dir({(o, "up", 1), (o, "down", 2), (o, "left", 1), (o, "right", 1)}))


if __name__ == "__main__":
    main()
