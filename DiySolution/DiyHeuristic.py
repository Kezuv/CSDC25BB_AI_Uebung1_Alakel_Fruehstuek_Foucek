# general declaration from superclass Heuristic
class Heuristic:
    def calculate_heuristic(self, cur):
        return 0


class Hamming(Heuristic):
    # contains the goal-puzzle
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    # calculate the heuristic distance with the count of each puzzle-tile which is in the false position
    def calculate_heuristic(self, cur):
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
    # contains the goal-puzzle
    def __init__(self, goal_puzzle):
        self.goal = goal_puzzle

    # calculate the heuristic distance with a counter of how many steps has each puzzle-tile
    # to move to their correct position
    def calculate_heuristic(self, cur):
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
        return 0
