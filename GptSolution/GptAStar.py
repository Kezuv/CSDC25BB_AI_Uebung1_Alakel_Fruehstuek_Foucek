from GptSolution.GptPriorityQueue import PriorityQueue
from GptSolution.GptNode import Node


def _reconstruct_path(node):
    path = []
    while node:
        path.append(node.puzzle.board)
        node = node.parent
    return path[::-1]


class AStar:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, initial_puzzle, goal_puzzle):
        start_node = Node(initial_puzzle)
        start_node.update_heuristic(self.heuristic.calculate(initial_puzzle, goal_puzzle))

        frontier = PriorityQueue()
        frontier.put(start_node, start_node.f)
        frontier_states = {tuple(map(tuple, start_node.puzzle.board))}  # Add start state to the set
        explored = set()

        while not frontier.is_empty():
            current_node = frontier.get()

            if current_node.puzzle.is_goal(goal_puzzle):
                return _reconstruct_path(current_node)

            explored.add(tuple(map(tuple, current_node.puzzle.board)))

            for neighbor in current_node.puzzle.get_neighbors():
                neighbor_state = tuple(map(tuple, neighbor.board))
                if neighbor_state in explored or neighbor_state in frontier_states:
                    continue

                neighbor_node = Node(neighbor, current_node, current_node.g + 1)
                neighbor_node.update_heuristic(self.heuristic.calculate(neighbor, goal_puzzle))

                frontier.put(neighbor_node, neighbor_node.f)
                frontier_states.add(neighbor_state)  # Add new state to the set

        return None

