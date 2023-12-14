class Node:

    def __init__(self, init_puzzle, init_cost, heuristic):
        self.curPuzzle = init_puzzle
        self.g = init_cost
        self.h = heuristic.calculate_heuristic(init_puzzle)
        self.childNodes = []

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def expand(self, heuristic):
        next_options = self.curPuzzle.extend()
        for puzzle in next_options:
            new_leaf_node = Node(puzzle, self.g+1, heuristic)
            self.childNodes.append(new_leaf_node)
        return self.childNodes

