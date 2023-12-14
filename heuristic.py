class Heuristic:
    def calculate_heuristic(self, cur):
        return 0


class Hammingway(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        return self.goal.count_misplaced_tiles(cur)

class Manhatten(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        return 1


class Euklid(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        return 2
