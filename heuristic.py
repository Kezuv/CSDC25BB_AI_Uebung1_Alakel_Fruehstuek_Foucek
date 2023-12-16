from puzzle import Puzzle
class Heuristic:
    def calculate_heuristic(self, cur):
        return 0


class Hammingway(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        goal_puzzle = self.goal
        misplaced_count = 0
        for i in range(len(goal_puzzle.board)):
            for j in range(len(goal_puzzle.board[i])):
                if goal_puzzle.board[i][j] != cur.board[i][j]:
                    misplaced_count += 1
        return misplaced_count

class Manhatten(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        distance = 0

        for i in range(len(self.goal.board)):
            for j in range(len(self.goal.board[i])):
                value = self.goal.board[i][j]
                if value != 0:
                    # Finde die Position der Zahl im anderen Puzzle
                    x, y = cur.find_position(value)

                    # Berechne die Manhattan-Distanz und addiere sie zur Gesamtdistanz
                    distance += abs(x - i) + abs(y - j)
        return distance

class Euklid(Heuristic):
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    def calculate_heuristic(self, cur):
        return 2
