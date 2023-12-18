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
        nextOptions = self.curPuzzle.extend()
        for node in nextOptions:
            self.childNodes.append(Node(node, self.g+1))
            self.h = heuristic.calculate_heuristic()

        return self.childNodes


"""import numpy as np
import random

#StateGenerator
class StateGenerator:
    @staticmethod
    def generate_state(seed=42):
        def is_solvable(state):
            inv_count = 0
            flat_state = state.flatten()
            for i in range(8):
                for j in range(i + 1, 9):
                    if flat_state[j] and flat_state[i] and flat_state[i] > flat_state[j]:
                        inv_count += 1
            return inv_count % 2 == 0

        random.seed(seed)
        while True:
            state = list(range(9))
            random.shuffle(state)
            state = np.array(state).reshape((3, 3))
            if is_solvable(state):
                return state

"""