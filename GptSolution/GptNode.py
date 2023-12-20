class Node:
    def __init__(self, puzzle, parent=None, path_cost=0, heuristic_cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.g = path_cost  # Cost from the start node
        self.h = heuristic_cost  # Heuristic cost
        self.f = self.g + self.h  # Total cost

    def update_heuristic(self, heuristic_cost):
        self.h = heuristic_cost
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.puzzle.board == other.puzzle.board

    # Additional methods as required...
