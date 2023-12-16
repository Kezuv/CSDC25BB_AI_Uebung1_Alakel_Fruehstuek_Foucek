class Node:

    def __init__(self, init_puzzle, init_cost, init_h):
        self.curPuzzle = init_puzzle
        self.g = init_cost
        self.h = init_h
        self.childNodes = []

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def expand(self, heuristic, previous_puzzles):
        next_options = self.curPuzzle.extend(previous_puzzles)
        for puzzle in next_options:
            new_leaf_node = Node(puzzle, self.g+1, heuristic.calculate_heuristic(puzzle))
            self.childNodes.append(new_leaf_node)
            previous_puzzles.append(new_leaf_node)
        return self.childNodes

