import random


class Puzzle:

    # puzzle contains a 2-D Array with values from 0 to 9
    def __init__(self, initial_state):
        self.board = initial_state

    # generates a random puzzle with values from 0 to 9
    @staticmethod
    def generate_random_puzzle():
        numbers = list(range(9))
        random.shuffle(numbers)
        random_puzzle = [numbers[i:i + 3] for i in range(0, 9, 3)]
        return Puzzle(random_puzzle)

    # return up to 4 leafs for Tree with new permutations from the puzzle
    def extend(self):
        newLeafs = []

        up_puzzle = self.move_up()
        if up_puzzle is not None:
            newLeafs.append(up_puzzle)

        down_puzzle = self.move_down()
        if down_puzzle is not None:
            newLeafs.append(down_puzzle)

        left_puzzle = self.move_left()
        if left_puzzle is not None:
            newLeafs.append(left_puzzle)

        right_puzzle = self.move_right()
        if right_puzzle is not None:
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


"""import numpy as np
# PuzzleState class
class PuzzleState:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = np.array(state)
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = 0
        self.blank_pos = self._find_blank()

    def update_total_cost(self):
        self.total_cost = self.path_cost + self.heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def _find_blank(self):
        return tuple(np.argwhere(self.state == 0)[0])

    def _swap(self, pos1, pos2):
        new_state = np.copy(self.state)
        new_state[pos1], new_state[pos2] = new_state[pos2], new_state[pos1]
        return new_state

    def get_neighbors(self):
        neighbors = []
        x, y = self.blank_pos
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

        for action, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = self._swap(self.blank_pos, (new_x, new_y))
                new_node = PuzzleState(new_state, self, action, self.path_cost + 1)
                neighbors.append(new_node)

        return neighbors"""