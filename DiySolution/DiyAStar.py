from DiySolution.DiyNode import Node
from DiySolution.DiyPriorityQueue import PriorityQueue
from DiySolution.DiyPuzzle import Puzzle
from DiySolution.DiyHeuristic import Heuristic


class AStar:
    """contains a step counter, the amount of time to calculate the best way and a priority queue"""
    def __init__(self):
        self.steps = 0
        self.depth = 0
        self.queue = PriorityQueue()

    # start the aStar algorythm with a puzzle to solve, and a heuristic function.
    def solve(self, init_puzzle, heuristic):
        """this solves the puzzles
        :param init_puzzle: the initial puzzle to be solved
        :type init_puzzle: Puzzle
        :param heuristic: the heuristic subclass that defines the distance function to be used
        :type heuristic: Heuristic
        :returns: statistic values: steps=times a node is taken from the queue; depth=depth of the solve tree
        :rtype: (int, int)
        """
        init_node = Node(init_puzzle, 0, heuristic.calculate_heuristic(init_puzzle))
        self.queue.put(init_node, 0, init_node.h)

        # initialize an array which will be contained all created puzzles, so none of them will be created two times
        previous_puzzles = [init_puzzle.board]

        # while queue is not empty - otherwise there is no way.
        while not self.queue.is_empty():
            # get the first item from queue
            current_node = self.queue.pop()

            # base case: if h == 0, we reached the goal-puzzle
            if current_node.h == 0:
                self.depth = current_node.g
                break
            else:
                previous_puzzles.append(current_node.curPuzzle.board)
                # create the child-nodes and put them in queue
                new_leafs = current_node.expand(heuristic)

                for leaf in new_leafs:
                    if self.is_leaf_new(leaf, previous_puzzles) is not True:
                        self.queue.put(leaf, leaf.g + leaf.h, leaf.h)
                # increase steps by 1
                self.steps += 1

        return self.steps, self.depth

    def is_leaf_new(self, leaf, previous_puzzles):
        """checks if a leaf puzzle was already looked at (is in previous_puzzles)
        :param leaf: a puzzle to check that was currently expanded
        :type leaf: Node
        :param previous_puzzles: all expanded puzzles that were put in the queue
        :type previous_puzzles: list
        :returns: if the leaf exists in previous_puzzles
        :rtype: bool
        """

        return leaf.curPuzzle.board in previous_puzzles
