class Heuristic:
    def calculate_heuristic(self, cur, goal):
        return 0


class Manhatten(Heuristic):
    def calculate_heuristic(self, cur, goal):
        return 1


class Euklid(Heuristic):
    def calculate_heuristic(self, cur, goal):
        return 2



"""import heapq, numpy as np
from PuzzleState import PuzzleState
#PuzzleSolver class
class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def hamming_distance(self, state):
        return np.sum(state.state != self.goal_state) - 1 if 0 in state.state else np.sum(state.state != self.goal_state)

    def manhattan_distance(self, state):
        state_coords = {val: (i, j) for i, row in enumerate(state.state) for j, val in enumerate(row)}
        goal_coords = {val: (i, j) for i, row in enumerate(self.goal_state) for j, val in enumerate(row)}
        return sum(abs(x - gx) + abs(y - gy) for val, (x, y) in state_coords.items() if val != 0 for gx, gy in [goal_coords[val]])

    def euclidean_distance(self, state):
        state_coords = {val: (i, j) for i, row in enumerate(state.state) for j, val in enumerate(row)}
        goal_coords = {val: (i, j) for i, row in enumerate(self.goal_state) for j, val in enumerate(row)}
        return sum(np.sqrt((x - gx)**2 + (y - gy)**2) for val, (x, y) in state_coords.items() if val != 0 for gx, gy in [goal_coords[val]])

    def solve(self, heuristic='manhattan'):
        start_node = PuzzleState(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (0, start_node))  # The priority queue item is a tuple (total_cost, PuzzleState)
        explored = set()

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)  # Unpack the tuple

            if np.array_equal(current_node.state, self.goal_state):
                return current_node

            explored.add(tuple(map(tuple, current_node.state)))

            for neighbor in current_node.get_neighbors():
                if tuple(map(tuple, neighbor.state)) in explored:
                    continue

                if heuristic == 'hamming':
                    neighbor.heuristic = self.hamming_distance(neighbor)
                elif heuristic == 'manhattan':
                    neighbor.heuristic = self.manhattan_distance(neighbor)
                elif heuristic == 'euclidean':
                    neighbor.heuristic = self.euclidean_distance(neighbor)

                neighbor.update_total_cost()
                heapq.heappush(frontier, (neighbor.total_cost, neighbor))  # Push as tuple (total_cost, PuzzleState)

        return None  # Return None if no solution is found

"""