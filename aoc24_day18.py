# setup
import copy
file = "./inputs/aoc24_day18_input.txt"
coordinates = []

# coordinates are X;Y pairs
# X horizontal from left, Y vertical from top


# we start 0,0
# we want to get to exit := 70,70 (real input) bzw 6,6 (example input)

def part1(coordinates, num_bytes):
    # function to simulate first X number of bytes falling and return minimum step number

# plan: (ab)use a python implementation of A* search/uniform-cost-search created as part of a uni course
# permalink of assignment (possibly private) : https://github.com/flowy-git/FIS/tree/cec32abd20ba03f3ae6011c32a0e48c634ae5991/programming_assignment_1

class Node:
    def __init__(self, state, parent, action, path_cost = 1):
        self.state = state # city name -> string
        self.parent = parent # parent city -> currently stored as Node object, might be extra overhead compared to storing name&hash
        self.action = action # action
        self.path_cost = path_cost # cost -> int

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __lt__(self, other):
        return self.path_cost > other.path_cost # not actually less than, but greater than, because we want decreasing order to be able to use pop()

class Action:
    def __init__(self, child_state, cost = 1):
        self.child_state = child_state # the city we go to
        self.cost = cost # the cost of the action

def subtask_1(problem):
    node = Node(problem['problem']['city_start'], 0, 0, 0) # initial state
    frontier = [node]
    explored_set = []
    while True:
        if len(frontier) == 0:
            raise ValueError("Subtask1_problem_issue_frontier_empty")
        node = frontier.pop() # takes last element, removes from frontier -> if ordered correctly, lowest cost
        if is_goal_state(problem, node.state):
            return solution(problem, node, len(explored_set)) # need to define and cosntruct node properly to obtain solution
        explored_set.append(node)
        for action in get_actions(problem, node.state):
            child = Node(action.child_state, node, action, (action.cost + node.path_cost))
            if (child not in explored_set) and (child not in frontier):
                frontier.append(child)
                # re-sort frontier???
                frontier.sort() # should work, we override the less_than op for Node
            elif (child in frontier):
                idx = frontier.index(child)
                if frontier[idx].path_cost > child.path_cost:
                    frontier[idx] = child

def get_actions(problem, node_state):
    actions = []
    for city, cost in problem['problem']['city_' + node_state]['connects_to'].items():
        action = Action(city, int(cost)) # need to see how yaml access works here # update: should work like this
        actions.append(action)
    return actions

def solution(problem, node, expanded):
    start_node = Node(problem['problem']['city_start'], 0, 0, 0)
    path = []
    current_node = node
    while current_node is not start_node and isinstance(current_node, Node):
        # take the node, work up towards start_node
        path.append(current_node.state)
        current_node = current_node.parent
    toreturn = len(path)
    return toreturn
    

def is_goal_state(problem, node_state):
    if problem['problem']['city_end'] == node_state:
        return True
    return False




# load & process input
with open(file) as aoc_input:
    patterns_done = False
    for line in aoc_input:
        line = line.split(",")
        coordinates.append(line)
    part1 = part1(coordinates, 12)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)