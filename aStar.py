import priorityQueue
from node import Node



class AStar:
    def __init__(self):
        self.steps = 0
        self.time = 0
        self.queue = priorityQueue.PriorityQueue()

    def start(self, init_puzzle, heuristic):
        init_node = Node(init_puzzle, 0, heuristic.calculate_heuristic(init_puzzle))
        self.queue.put(init_node, 0)

        previous_puzzles = [init_puzzle]
        while not self.queue.is_empty():
            current_node = self.queue.get()
            print('Heurisitc:' + str(current_node.h) + '________ Cost: ' + str(current_node.g) + '_________ Sum:' + str(current_node.h + current_node.g))
            if current_node.h == 0:
                break
            else:
                new_leafs = current_node.expand(heuristic, previous_puzzles)
                for leaf in new_leafs:
                    self.queue.put(leaf, leaf.g + leaf.h)

                self.steps += 1

        return self.steps, self.time
