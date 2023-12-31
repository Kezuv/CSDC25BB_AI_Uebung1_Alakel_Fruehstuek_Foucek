class Node:
    """node class that contains a current puzzle, stop-cost (g), heuristic costs (h) and an array for child-nodes"""
    def __init__(self, init_puzzle, init_cost, init_h):
        self.curPuzzle = init_puzzle
        self.g = init_cost
        self.h = init_h
        self.childNodes = []

    # makes the node comparable to its overall cost.
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    #
    def expand(self, heuristic):
        """Expands the node with new leaf-nodes that contains all different possible puzzle-boards from the current one."""
        next_options = self.curPuzzle.extend()
        for puzzle in next_options:
            # create new nodes for each new puzzle with the calculated heuristic distance and increase g by 1
            new_leaf_node = Node(puzzle, self.g+1, heuristic.calculate_heuristic(puzzle))
            self.childNodes.append(new_leaf_node)
        return self.childNodes
