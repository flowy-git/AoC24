# setup
import copy
file = "./inputs/aoc24_day16_input.txt"

# we've already done a maze solving implementation for day 18, adapting uniform-cost-search
# idea : copy & adapt the function from aoc24_day18


coordinates = []
map = []
X = 0
Y = 0

# coordinates are X;Y pairs
# X horizontal from left, Y vertical from top


# we start (X-1, 1)
# we want to get to exit := (1, Y-1)

def part1(coordinates):
    #X = N
    #Y = N
    problem = [[x, y] for x in range(X+1) for y in range(Y+1)]
    blacklist = coordinates
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
        self.f_score = self.path_cost + self.heuristic([1, Y-1])

    def heuristic(self, goal):
        # manhattan distance
        return abs(self.state[0] - goal[0]) + abs(self.state[1] - goal[1])

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Action:
    def __init__(self, child_state, cost = 1):
        self.child_state = child_state # the city we go to
        self.cost = cost # the cost of the action

def subtask_1(problem, blacklist):
    node = Node([1, Y-1], Node([0, Y-1], 0, 0, 0), 0, 0) # initial state -> Position X,Y = 0,0 # added "parent" to have starting direction
    frontier = [node]
    explored_set = []
    #for i in frontier:
    #    print(i.state)
    print("########## STARTING #############")
    while True:
        #print("///// CURRENT FRONTIER //////")
        #for i in frontier:
        #    print(i.state)
        if len(frontier) == 0:
            raise ValueError("Subtask1_problem_issue_frontier_empty")
        node = frontier.pop(0)
        if node.state == [X-1, 1]:
            print("solution found")
            return solution(problem, node)
        explored_set.append(node)
        for action in get_actions(problem, node.state, blacklist, node.parent):
            #print(action)
            child = Node(action.child_state, node, action, action.cost)
            if (child not in explored_set) and (child not in frontier):
                frontier.append(child)
                # re-sort frontier???
                frontier.sort() # should work, we override the less_than op for Node
            elif (child in frontier):
                idx = frontier.index(child)
                if frontier[idx].path_cost > child.path_cost:
                    frontier[idx] = child
                frontier.sort()

def get_actions(problem, node_state, blacklist, node_parent):
    varX = node_state[0]
    varY = node_state[1]
    possible_actions = [[varX, varY+1], [varX+1, varY], [varX, varY-1], [varX-1, varY]]
    ranges_x = list(range(X + 1))
    ranges_y = list(range(Y + 1))
    actions = []
    for action in possible_actions:
        if action not in blacklist:
            if action[0] in ranges_x and action[1] in ranges_y:
                if action[0] == node_state[0] == node_parent.state[0] or action[1] == node_state[1] == node_parent.state[1]:
                    cost = 1
                else:
                    cost = 1001
                actions.append(Action(action, cost))
    return actions

def solution(problem, node):
    total_cost = 0
    start_node = Node([1, Y-1], 0, 0, 0)
    path = []
    current_node = node
    while current_node is not start_node and isinstance(current_node, Node):
        total_cost += current_node.path_cost
        # take the node, work up towards start_node
        path.append(current_node.state)
        current_node = current_node.parent
    return path, total_cost

def digitise_map(map):
    toreturn = []
    for idx in range(X+1):
        for idy in range(Y+1):
            if map[idx][idy] == '#':
                toreturn.append([idy, idx])
    return toreturn

# load & process input
with open(file) as aoc_input:
    for line in aoc_input:
        Y += 1
        X = len(line)
        line = line.replace("\n", "")
        line = list(line)
        map.append(line)
    print("map len", len(map))
    Y -= 1
    X -= 1
    print("X", X)
    print("y", Y)
    coordinates = digitise_map(map)
    #print(coordinates)
    solution_path, cost = part1(coordinates)
    #print(solution_path)
    print(cost)
    part1 = cost

# print results
print("Part 1: ", part1)
#print("Part 2: ", part2)