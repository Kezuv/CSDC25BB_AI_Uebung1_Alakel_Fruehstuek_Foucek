import random


class Puzzle:

    # puzzle contains a 2-D Array with values from 0 to 9
    def __init__(self, initial_state):
        self.board = initial_state

    # function that allows to iterate over the board.
    def __iter__(self):
        return iter(self.board)

    # made puzzles comparable
    # def __eq__(self, other):
    #     return self.board == other.board

    # generates a random puzzle with values from 0 to 9
    @staticmethod
    def generate_random_puzzle(seed, puzzle_count):
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

    # generates the goal-puzzle
    @staticmethod
    def generate_goal_puzzle():
        return Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    # This function returns true
    # if given 8 puzzle is solvable.

    def is_solvable(self):

        # Count inversions in given 8 puzzle
        inv_count = self.get_inv_count([j for sub in self.board for j in sub])

        # return true if inversion count is even.
        return inv_count % 2 == 0

    # A utility function to count
    # inversions in given array 'arr[]'
    def get_inv_count(self, arr):
        inv_count = 0
        empty_value = 0

        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    # return up to 4 leafs for the tree with new permutations from the puzzle which where not created before
    def extend(self):
        new_leafs = []


        up_puzzle = self.move_up()
        if up_puzzle is not None and up_puzzle:
            new_leafs.append(up_puzzle)

        down_puzzle = self.move_down()
        if down_puzzle is not None and down_puzzle:
            new_leafs.append(down_puzzle)

        left_puzzle = self.move_left()
        if left_puzzle is not None and left_puzzle:
            new_leafs.append(left_puzzle)

        right_puzzle = self.move_right()
        if right_puzzle is not None and right_puzzle:
            new_leafs.append(right_puzzle)

        return new_leafs

    # print out the puzzle as a 3x3 matrix
    def display(self):
        for row in self.board:
            print(row)

    # finds the blank field "0" and return the coordination
    def find_blank(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    # find a specific position of a puzzle-tile (number)
    def find_position(self, value):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == value:
                    return i, j

    # following functions switch the puzzle-tile with "0" with their neighbours and return a new puzzle-board.
    # If the move is not possible return = none
    def move_up(self):
        tmp_puzzle = Puzzle([row[:] for row in self.board])

        blank_row, blank_col = tmp_puzzle.find_blank()
        if blank_row > 0:
            tmp_puzzle.board[blank_row][blank_col], tmp_puzzle.board[blank_row - 1][blank_col] = \
                tmp_puzzle.board[blank_row - 1][blank_col], tmp_puzzle.board[blank_row][blank_col]
            return tmp_puzzle
        else:
            return None

    def move_down(self):
        tmp_puzzle = Puzzle([row[:] for row in self.board])

        blank_row, blank_col = tmp_puzzle.find_blank()
        if blank_row < 2:
            tmp_puzzle.board[blank_row][blank_col], tmp_puzzle.board[blank_row + 1][blank_col] = \
                tmp_puzzle.board[blank_row + 1][blank_col], tmp_puzzle.board[blank_row][blank_col]
            return tmp_puzzle
        else:
            return None

    def move_left(self):
        tmp_puzzle = Puzzle([row[:] for row in self.board])

        blank_row, blank_col = tmp_puzzle.find_blank()
        if blank_col > 0:
            tmp_puzzle.board[blank_row][blank_col], tmp_puzzle.board[blank_row][blank_col - 1] = \
                tmp_puzzle.board[blank_row][blank_col - 1], tmp_puzzle.board[blank_row][blank_col]
            return tmp_puzzle
        else:
            return None

    def move_right(self):
        tmp_puzzle = Puzzle([row[:] for row in self.board])

        blank_row, blank_col = tmp_puzzle.find_blank()
        if blank_col < 2:
            tmp_puzzle.board[blank_row][blank_col], tmp_puzzle.board[blank_row][blank_col + 1] = \
                tmp_puzzle.board[blank_row][blank_col + 1], tmp_puzzle.board[blank_row][blank_col]
            return tmp_puzzle
        else:
            return None
