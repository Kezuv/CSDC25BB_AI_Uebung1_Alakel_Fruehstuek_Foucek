import random


class Puzzle:
    """Holds the board and functionality for moving tiles
    :var board: a 2D array with values from 0 to 9
    :var blank_pos: the position of the blank tile
    """
    def __init__(self, board):
        self.board = board
        self.blank_pos = self._find_blank()

    def _find_blank(self):
        """Finds the position of the blank tile
        :return: the position of the blank tile
        :rtype: int
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i, j)
        raise ValueError("No blank space (0) found in the puzzle.")

    def move_blank(self, direction):
        """Moves the blank tile in the specific direction
        :param direction: the direction name for moving the blank tile
        :type direction: str
        """
        x, y = self.blank_pos
        if direction == "up" and x > 0:
            self._swap((x - 1, y))
        elif direction == "down" and x < len(self.board) - 1:
            self._swap((x + 1, y))
        elif direction == "left" and y > 0:
            self._swap((x, y - 1))
        elif direction == "right" and y < len(self.board[0]) - 1:
            self._swap((x, y + 1))

    def _swap(self, pos):
        """Swaps two tiles
        :param pos: the direction name for moving the blank tile
        :type pos: tuple
        """
        bx, by = self.blank_pos
        nx, ny = pos
        self.board[bx][by], self.board[nx][ny] = self.board[nx][ny], self.board[bx][by]
        self.blank_pos = pos

    def get_neighbors(self):
        """Gets all neighbor puzzles around the puzzle
        :return: the neigbor puzzles around the puzzle
        :rtype: list
        """
        neighbors = []
        for direction in ["up", "down", "left", "right"]:
            new_puzzle = Puzzle([row[:] for row in self.board])
            new_puzzle.move_blank(direction)
            if new_puzzle.blank_pos != self.blank_pos:  # If blank tile moved
                neighbors.append(new_puzzle)
        return neighbors

    def is_goal(self, goal_state):
        return self.board == goal_state

    def is_solvable(self):
        """Check if the puzzle is solvable
        :return: if the puzzle is solvable
        :rtype: bool
        """
        flat_board = [num for row in self.board for num in row if num != 0]
        inversions = 0
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversions += 1
        return inversions % 2 == 0

    @staticmethod
    def generate_random_puzzle(seed, puzzle_count):
        """Generates a number of random puzzles based a given seed
        :param seed: the seed used for the random generator
        :type seed: int
        :param puzzle_count: number of puzzles to be generated
        :type puzzle_count: int
        :return: a list of solveable puzzles
        :rtype: list
        """
        generated_puzzles = []
        while generated_puzzles.__len__() < puzzle_count:
            numbers = list(range(9))
            random.seed(seed)
            random.shuffle(numbers)
            temp_puzzle = Puzzle([numbers[i:i + 3] for i in range(0, 9, 3)])
            if temp_puzzle.is_solvable():
                generated_puzzles.append(temp_puzzle)
            seed += 1
        return generated_puzzles
