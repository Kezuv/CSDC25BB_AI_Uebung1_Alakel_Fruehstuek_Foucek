from math import sqrt


class Heuristic:
    def calculate(self, puzzle, goal):
        raise NotImplementedError("This method should be overridden by subclasses")


class HammingDistance(Heuristic):
    def calculate(self, puzzle, goal):
        mismatch = 0
        for i in range(3):
            for j in range(3):
                if puzzle.board[i][j] != goal[i][j] and puzzle.board[i][j] != 0:
                    mismatch += 1
        return mismatch


class ManhattanDistance(Heuristic):
    def calculate(self, puzzle, goal):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                tile = puzzle.board[i][j]
                if tile != 0:
                    # Find the tile's position in the goal state
                    for gi in range(3):
                        for gj in range(3):
                            if goal[gi][gj] == tile:
                                total_distance += abs(gi - i) + abs(gj - j)
                                break
        return total_distance


class EuclideanDistance(Heuristic):
    def calculate(self, puzzle, goal):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                tile = puzzle.board[i][j]
                if tile != 0:
                    # Find the tile's position in the goal state
                    for gi in range(3):
                        for gj in range(3):
                            if goal[gi][gj] == tile:
                                total_distance += sqrt((gi - i) ** 2 + (gj - j) ** 2)
                                break
        return total_distance
