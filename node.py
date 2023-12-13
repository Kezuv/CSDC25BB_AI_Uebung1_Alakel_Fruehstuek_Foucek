import puzzle as p


class Node:
    childNodes = []
    curPuzzle = p.Puzzle
    g = 0
    h = 0

    def __init__(self, init_puzzle, init_cost):
        self.curPuzzle = init_puzzle
        self.g = init_cost

    def expand(self, heuristic):
        nextOptions = self.curPuzzle.expension()
        for node in nextOptions:
            self.childNodes.append(Node(node, self.g+1))
            self.h = heuristic.calculate_heuristic()

        return self.childNodes

