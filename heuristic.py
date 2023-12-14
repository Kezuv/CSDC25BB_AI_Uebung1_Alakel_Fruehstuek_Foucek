class Heuristic:
    def calculate_heuristic(self, cur, goal):
        return 0


class Manhatten(Heuristic):
    def calculate_heuristic(self, cur, goal):
        return 8


class Euklid(Heuristic):
    def calculate_heuristic(self, cur, goal):
        return 2
