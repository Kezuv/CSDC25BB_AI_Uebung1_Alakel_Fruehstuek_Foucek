import heapq
from GptSolution.GptNode import Node


class PriorityQueue:
    """Holds the nodes of the queue and gives functions for interacting with the queue
    :var elements: the nodes in the queue
    """
    def __init__(self):
        self.elements = []

    def is_empty(self):
        """Checks if the queue is empty
        :returns: if the queue is empty
        :rtype: bool
        """
        return len(self.elements) == 0

    def put(self, item, priority):
        """Puts a new node sorted in the queue
        :param item: the node itself
        :type item: Node
        :param priority: the priority of the node
        :type priority: int
        """
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """Pops the first node in the queue
        :returns: the first node in the queue
        :rtype: Node
        """
        return heapq.heappop(self.elements)[1]
