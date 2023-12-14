import queue
from node import Node



class AStar:
    def __init__(self):
        self.steps = 0
        self.time = 0
        self.queue = queue.Queue()

    def start(self, init_puzzle, heuristic):
        init_node = Node(init_puzzle, 0, heuristic)
        self.queue.put(init_node, 0)

        while not self.queue.is_empty():
            current_node = self.queue.get()
            current_node.curPuzzle.display()
            if current_node.h == 0:
                break
            else:
                new_leafs = current_node.expand(heuristic)
                for leaf in new_leafs:
                    self.queue.put(leaf, leaf.g + leaf.h)

                self.steps += 1

        return self.steps, self.time
