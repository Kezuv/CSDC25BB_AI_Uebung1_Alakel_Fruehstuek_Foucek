import random


class Puzzle:

    # puzzle contains a 2-D Array with values from 0 to 9
    def __init__(self, initial_state):
        self.board = initial_state

    def __iter__(self):
        return iter(self.board)

    # generates a random puzzle with values from 0 to 9
    @staticmethod
    def generate_random_puzzle():
        numbers = list(range(9))
        random.shuffle(numbers)
        random_puzzle = [numbers[i:i + 3] for i in range(0, 9, 3)]
        return Puzzle(random_puzzle)

    @staticmethod
    def generate_goal_puzzle():
        return Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    # return up to 4 leafs for Tree with new permutations from the puzzle
    def extend(self, previous_puzzles):
        newLeafs = []

        up_puzzle = self.move_up()
        if up_puzzle is not None and up_puzzle not in previous_puzzles:
            newLeafs.append(up_puzzle)

        down_puzzle = self.move_down()
        if down_puzzle is not None and down_puzzle not in previous_puzzles:
            newLeafs.append(down_puzzle)

        left_puzzle = self.move_left()
        if left_puzzle is not None and left_puzzle not in previous_puzzles:
            newLeafs.append(left_puzzle)

        right_puzzle = self.move_right()
        if right_puzzle is not None and right_puzzle not in previous_puzzles:
            newLeafs.append(right_puzzle)

        return newLeafs

    # print out the puzzle as a 3x3 matrix
    def display(self):
        for row in self.board:
            print(row)

    # finds the blank field "0" and return coordination
    def find_blank(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    def find_position(self, value):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == value:
                    return i, j

    # following switch the tile with "0" with their neighbours and return a new Puzzle.
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


# randomPuzzle = Puzzle([[1, 5, 3], [4, 0, 7], [6, 8, 2]])
# randomPuzzle.display()
# print('---------')

# listOfPuzzle = randomPuzzle.extend()
# for i in listOfPuzzle:
#     i.display()
#     print('---------')
