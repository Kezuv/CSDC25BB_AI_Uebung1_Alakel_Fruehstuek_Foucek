from math import sqrt
from GptSolution.GptPuzzle import Puzzle


class Heuristic:
    """Holds the heuristic functions for distance calculations"""
    def calculate(self, puzzle, goal):
        """calculates the heuristic distance from a given puzzle to the given goal puzzle
        :param puzzle: the puzzle that is beeing calculated
        :type puzzle: Puzzle
        :param goal: the goal puzzle
        :type goal: int[][]
        :returns: heuristic distance
        :rtype: int
        """
        raise NotImplementedError("This method should be overridden by subclasses")


class HammingDistance(Heuristic):
    """Holds the heuristic functions for hamming-distance calculations"""
    # calculate the heuristic distance by the count of wrong placed tiles
    def calculate(self, puzzle, goal):
        mismatch = 0
        for i in range(3):
            for j in range(3):
                if puzzle.board[i][j] != goal[i][j] and puzzle.board[i][j] != 0:
                    mismatch += 1
        return mismatch


class ManhattanDistance(Heuristic):
    """Holds the heuristic functions for manhattan-distance calculations"""
    # calculate the heuristic distance by only allowing horizontal and vertical moves
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
    """Holds the heuristic functions for euclidean-distance calculations"""
    # calculate the heuristic distance by using the pythagoras theorem
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
