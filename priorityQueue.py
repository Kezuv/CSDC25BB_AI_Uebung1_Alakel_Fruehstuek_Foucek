class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        entry = (item, priority)
        index = 0

        # Suche die Position, an der das Element eingefügt werden soll
        while index < len(self.elements) and priority > self.elements[index][1]:
            index += 1

        # Füge das Element an der gefundenen Position ein
        self.elements.insert(index, entry)

    def get(self):
        if not self.is_empty():
            return self.elements.pop(0)[0]
