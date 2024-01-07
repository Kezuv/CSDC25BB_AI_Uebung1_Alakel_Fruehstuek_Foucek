from GptSolution.GptNode import Node
from GptSolution.GptPriorityQueue import PriorityQueue


# not used
def _reconstruct_path(node):
    path = []
    while node:
        path.append(node.puzzle.board)
        node = node.parent
    return path[::-1]


class AStar:
    """contains a reference to the heuristic function that is beeing used
    and a step and detph counter for statistic evaluation"""
    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.steps = 0
        self.depth = 0

    def solve(self, initial_puzzle, goal_puzzle):
        """this solves the puzzles
        :param initial_puzzle: the initial puzzle to be solved
        :type initial_puzzle: Puzzle
        :param goal_puzzle: the goal puzzle
        :type goal_puzzle: String[][]
        :returns: statistic values: steps=times a node is taken from the queue; depth=depth of the solve tree
        :rtype: (int, int)
        """
        start_node = Node(initial_puzzle)
        start_node.update_heuristic(self.heuristic.calculate(initial_puzzle, goal_puzzle))

        # initializes the priority queue
        frontier = PriorityQueue()
        frontier.put(start_node, start_node.f)
        frontier_states = {tuple(map(tuple, start_node.puzzle.board))}  # Add start state to the set

        # initializes the set for already explored puzzles
        explored = set()

        # while the queue is not
        while not frontier.is_empty():
            # get first puzzle in the queue and check if it is the goal puzzle
            current_node = frontier.get()
            if current_node.puzzle.is_goal(goal_puzzle):
                self.depth = current_node.g
                break

            # add puzzle to the explored set
            explored.add(tuple(map(tuple, current_node.puzzle.board)))

            # loop through every neighbor puzzle
            for neighbor in current_node.puzzle.get_neighbors():
                neighbor_state = tuple(map(tuple, neighbor.board))

                # ignore already explored puzzles
                if neighbor_state in explored or neighbor_state in frontier_states:
                    continue


                neighbor_node = Node(neighbor, current_node, current_node.g + 1)
                neighbor_node.update_heuristic(self.heuristic.calculate(neighbor, goal_puzzle))

                # put the neighbor in the queue
                frontier.put(neighbor_node, neighbor_node.f)
                frontier_states.add(neighbor_state) # Add new state to the set

            # update steps
            self.steps += 1
        return self.steps, self.depth
