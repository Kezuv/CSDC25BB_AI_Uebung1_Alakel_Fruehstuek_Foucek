# general declaration from superclass Heuristic
from math import sqrt


class Heuristic:
    """Contains the heuristic logic of different algorithms"""
    def calculate_heuristic(self, cur):
        return 0


class Hamming(Heuristic):
    """contains the goal-puzzle"""
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    # calculate the heuristic distance with the count of each puzzle-tile which is in the false position
    def calculate_heuristic(self, cur):
        """Calculates the heuristic distance of the given state of the puzzle."""
        goal_puzzle = self.goal
        misplaced_count = 0
        for i in range(len(cur.board)):
            for j in range(len(cur.board[i])):
                if (cur.board[i][j]) and (goal_puzzle.board[i][j] != cur.board[i][j]):
                    misplaced_count += 1
        return misplaced_count


class Haming_WithBlank(Heuristic):
    # contains the goal-puzzle
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    # calculate the heuristic distance with the count of each puzzle-tile which is in the false position
    def calculate_heuristic(self, cur):
        goal_puzzle = self.goal
        misplaced_count = 0
        for i in range(len(cur.board)):
            for j in range(len(cur.board[i])):
                if goal_puzzle.board[i][j] != cur.board[i][j]:
                    misplaced_count += 1
        return misplaced_count


class Manhattan(Heuristic):
    """contains the goal-puzzle"""
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    # calculate the heuristic distance with a counter of how many steps has each puzzle-tile
    # to move to their correct position
    def calculate_heuristic(self, cur):
        """calculates the Manhattan distance for the given board"""
        distance = 0

        for i in range(len(self.goal.board)):
            for j in range(len(self.goal.board[i])):
                value = self.goal.board[i][j]
                if value != 0:
                    # find the position of the number in the current puzzle
                    x, y = cur.find_position(value)

                    # calculate the Manhattan distance and add it to the total distance
                    distance += abs(x - i) + abs(y - j)
        return distance


class Euclidean(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        """calculates the Euclidean distance for the given board"""
        total_distance = 0
        for goal_x in range(len(self.goal.board)):
            for goal_y in range(len(self.goal.board[goal_x])):
                value = self.goal.board[goal_x][goal_y]
                if value != 0:
                    for current_x in range(len(cur.board)):
                        for current_y in range(len(cur.board[current_x])):
                            if cur.board[current_x][current_y] == value:
                                total_distance += sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)
                                break
        return total_distance
