import time
from DiySolution.DiyNode import Node
from DiySolution.DiyPriorityQueue import PriorityQueue


class AStar:
    # contains a step counter, the amount of time to calculate the best way and a priority queue
    def __init__(self):
        self.steps = 0
        self.time = 0
        self.queue = PriorityQueue()

    # start the aStar algorythm with a puzzle to solve, and a heuristic function.
    def start(self, init_puzzle, heuristic):
        init_node = Node(init_puzzle, 0, heuristic.calculate_heuristic(init_puzzle))
        self.queue.put(init_node, 0, init_node.h)

        # initialize an array which will be contained all created puzzles, so none of them will be created two times
        previous_puzzles = [init_puzzle]

        start_time = time.time()

        # while queue is not empty - otherwise there is no way.
        while not self.queue.is_empty():
            # get the first item from queue
            current_node = self.queue.pop()

            # print stats from that node
            #print('Heurisitc:' + str(current_node.h) + '________ Cost: ' + str(current_node.g) + '_________ Sum:' + str(
            #     current_node.h + current_node.g))

            # base case - if h == 0, we reached the goal-puzzle
            if current_node.h == 0:
                break
            else:
                previous_puzzles.append(current_node.curPuzzle)
                # create the child-nodes and put them in queue
                new_leafs = current_node.expand(heuristic)
                for leaf in new_leafs:
                    if leaf.curPuzzle in previous_puzzles:
                        continue
                    self.queue.put(leaf, leaf.g + leaf.h, leaf.h)
                # increase steps by 1
                self.steps += 1
        # return step and time counter

        end_time = time.time()
        self.time = end_time - start_time

        return self.steps, self.time
