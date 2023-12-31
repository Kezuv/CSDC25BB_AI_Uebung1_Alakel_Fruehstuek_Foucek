from DiySolution.DiyNode import Node
from DiySolution.DiyPriorityQueue import PriorityQueue


class AStar:
    """contains a step counter, the amount of time to calculate the best way and a priority queue"""
    def __init__(self):
        self.steps = 0
        self.depth = 0
        self.queue = PriorityQueue()

    # start the aStar algorythm with a puzzle to solve, and a heuristic function.
    def solve(self, init_puzzle, heuristic):
        """this solves the puzzles
            it takes as parameter:
                - init_puzzle: the given puzzle to be solved
                - heuristic: the heuristic algorithm it needs to solve with """

        init_node = Node(init_puzzle, 0, heuristic.calculate_heuristic(init_puzzle))
        self.queue.put(init_node, 0, init_node.h)

        # initialize an array which will be contained all created puzzles, so none of them will be created two times
        previous_puzzles = [init_puzzle.board]

        # queue has to be empty - otherwise there is no way.
        while not self.queue.is_empty():
            # take the first item in consideration from queue and remove it:
            current_node = self.queue.pop()

            # base case: if h == 0, we reached the goal-puzzle
            if current_node.h == 0:
                self.depth = current_node.g
                break
            else:
                previous_puzzles.append(current_node.curPuzzle.board)
                # create the child-nodes and put them in queue:
                new_leafs = current_node.expand(heuristic)
                # for leaf in new_leafs:
                #     if leaf.curPuzzle.board in previous_puzzles:
                #         continue
                for leaf in new_leafs:
                    if self.is_leaf_new(leaf, previous_puzzles) is not True:
                        self.queue.put(leaf, leaf.g + leaf.h, leaf.h)

                self.steps += 1     # increase steps by 1

        return self.steps, self.depth

    def is_leaf_new(self, leaf, previous_puzzles):
        """checks if the board has been explored already."""
        found = False
        if leaf.curPuzzle.board in previous_puzzles:
            found = True

        return found
