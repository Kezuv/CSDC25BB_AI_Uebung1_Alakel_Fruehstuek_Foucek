class PriorityQueue:
    # priority queue contains a array
    def __init__(self):
        self.elements = []

    # return true when the queue is empty
    def is_empty(self):
        return len(self.elements) == 0

    # put items (nodes) with their priority (total cost) in the correct index
    def put(self, item, priority):
        entry = (item, priority)
        index = 0

        # find the position where the element should be inserted
        while index < len(self.elements) and priority > self.elements[index][1]:
            index += 1

        # Insert the element at the found position
        self.elements.insert(index, entry)

    # return the first node in queue.
    def get(self):
        if not self.is_empty():
            return self.elements.pop(0)[0]
