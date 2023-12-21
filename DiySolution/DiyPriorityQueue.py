import bisect
class PriorityQueue:
    # priority queue contains a array
    def __init__(self):
        self.elements = []

    # return true when the queue is empty
    def is_empty(self):
        return len(self.elements) == 0

    # put items (nodes) with their priority (total cost) in the correct index
    def put(self, node, priority, heuristic_value):
        entry = (priority, heuristic_value, node)
        # index = 0

        # find the position where the element should be inserted
        # Causes time problems
        # while index < len(self.elements) and (priority > self.elements[index][1] or heuristic_value > self.elements[index][2]):
        #    index += 1

        # while index < len(self.elements):
        #    if self.elements[index][1] < priority:
        #            index += 1

        # Insert the element at the found position
        # self.elements.insert(index, entry)

        bisect.insort(self.elements, entry)
    # return the first node in queue.
    def pop(self):
        if not self.is_empty():
            return self.elements.pop(0)[2]
