# setup
import copy
file = "./inputs/aoc24_day18_input.txt"
coordinates = []

# coordinates are X;Y pairs
# X horizontal from left, Y vertical from top


# we start 0,0
# we want to get to exit := 70,70 (real input) bzw 6,6 (example input)

def part1(coordinates, num_bytes):
    X = 6
    Y = 6
    problem = [[x, y] for x in range(X+1) for y in range(Y+1)]
    blacklist = coordinates[:num_bytes]
    toreturn = subtask_1(problem, blacklist)
    return toreturn
    # function to simulate first X number of bytes falling and return minimum step number

# plan: (ab)use a python implementation of A* search/uniform-cost-search created as part of a uni course
# permalink of assignment (possibly private) : https://github.com/flowy-git/FIS/tree/cec32abd20ba03f3ae6011c32a0e48c634ae5991/programming_assignment_1

class Node:
    def __init__(self, state, parent, action, path_cost = 1):
        self.state = state # we mod state to be a [X,Y] list
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

def subtask_1(problem, blacklist):
    node = Node([0,0], 0, 0, 0) # initial state -> Position X,Y = 0,0
    frontier = [node]
    explored_set = []
    while True:
        if len(frontier) == 0:
            raise ValueError("Subtask1_problem_issue_frontier_empty")
        #else:
            #print("frontier len fine\n")
            #print(len(frontier))
            #print("\n")
        node = frontier.pop() # takes last element, removes from frontier -> if ordered correctly, lowest cost
        #if is_goal_state(problem, node.state):
        ########## TEST CASE ONLY GOAL STATE -> NEED TO CHANGE TO 1024 OR OTHER
        if node.state == [6,6]:
        ########## TEST CASE ONLY GOAL STATE
            print("solution found")
            return solution(problem, node) # need to define and cosntruct node properly to obtain solution
        explored_set.append(node)
        for action in get_actions(problem, node.state, blacklist):
            #print(action)
            child = Node(action.child_state, node, action)
            if (child not in explored_set) and (child not in frontier):
                frontier.append(child)
                # re-sort frontier???
                frontier.sort() # should work, we override the less_than op for Node
            elif (child in frontier):
                idx = frontier.index(child)
                if frontier[idx].path_cost > child.path_cost:
                    frontier[idx] = child

def get_actions(problem, node_state, blacklist):
    #print("get actions triggered")
    X = node_state[0]
    Y = node_state[1]
    # this is how we define what steps we can take from a given position
    # idea: given coordiantes of node_state being X,Y
    # line up [X, Y+1], [X+1, Y], [X, Y-1], [X-1, Y]
    # maintain a blacklist of positions: all fallen bytes, and out of bounds positions
    # if not in those, return
    possible_actions = [[X, Y+1], [X+1, Y], [X, Y-1], [X-1, Y]]
    ranges = list(range(7))
    actions = []
    #print("possible actions : ", possible_actions)
    #print("ranges : ", ranges)
    #print("vlacklist : ", blacklist)
    
    for action in possible_actions:
        #print("action to verifz : ", action)
        if action not in blacklist:
            #print("action not in blacklist")
            #print("action X : ", action[0])
            #print("action Y : ", action[1])
            if action[0] in ranges and action[1] in ranges:
                #print("action cleared ranges")
                actions.append(Action(action))
    #print("actions to be returned : ", actions)
    return actions

def solution(problem, node):
    start_node = Node([0,0], 0, 0, 0)
    path = []
    current_node = node
    while current_node is not start_node and isinstance(current_node, Node):
        # take the node, work up towards start_node
        path.append(current_node.state)
        current_node = current_node.parent
    return path

# load & process input
with open(file) as aoc_input:
    patterns_done = False
    for line in aoc_input:
        line = line.replace("\n", "")
        line = line.split(",")
        line = [int(value) for value in line]
        coordinates.append(line)
    solution_path = part1(coordinates, 12)
    part1 = len(solution_path) - 1 # number of steps = path nodes - 1
    #print(solution_path)

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)