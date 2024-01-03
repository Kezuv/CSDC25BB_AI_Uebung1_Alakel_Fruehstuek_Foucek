class Node:
    """Holds information about the puzzle for the astar algorithm
    :var puzzle: the puzzle of the node
    :var parent: the puzzle of the node
    :var g: cost from the start node
    :var h: heuristic cost
    :var f: total cost
    """
    def __init__(self, puzzle, parent=None, path_cost=0, heuristic_cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.g = path_cost
        self.h = heuristic_cost
        self.f = self.g + self.h

    def update_heuristic(self, heuristic_cost):
        """updates the heuristic and total cost of the node
        :param: heuristic_cost: the new heuristic cost
        :type heuristic_cost: int
        """
        self.h = heuristic_cost
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.puzzle.board == other.puzzle.board
