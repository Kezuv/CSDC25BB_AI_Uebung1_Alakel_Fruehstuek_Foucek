import heapq

class Queue:
    """manages the node queue for A* algorithm"""
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# Example usage
#queue = Queue()
#queue.put("node1", 5)
#queue.put("node2", 3)
#queue.put("node3", 10)

#while not queue.is_empty():
 #   item = queue.get()
  #  print(item)