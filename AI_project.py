from collections import deque


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# get start - end params
print(color.BOLD +color.YELLOW+"please enter your board limited:"+color.END)
board_limit = int(input(color.BOLD +color.PURPLE+'your board limited is :'))
board_limited = board_limit - 1;
print(color.BOLD +color.YELLOW+"enter position x ,y . if you want =>(1,2),write in this shape => 1,2"+color.END)
start_node = tuple([int(x) for x in input(color.BOLD +color.PURPLE+'start node :'+color.END).split(",")])
target_node = tuple([int(x) for x in input(color.BOLD +color.PURPLE+'target node :'+color.END).split(",")])

print(color.BOLD +color.YELLOW+"enter your considered Limit for IDS algorithm"+color.END)
limit = int(input(color.BOLD +color.PURPLE+"yor considered Limit is :"+color.END))
print()
# get white params
print(color.BOLD +color.YELLOW+"enter white nodes ,for example (1,2),(3,6),(4,9)....  write in this shape => 1,2 3,6 4,9"+color.END)
fiiled_nodes = input(color.BOLD +color.PURPLE+"white nodes :"+color.END).split()
arr = []

for pos in fiiled_nodes:

    arr.append(tuple([int(x) for x in pos.split(",")]))


arr.insert(0, start_node)
arr.append(target_node)

# Test Case
# print(color.BOLD +color.YELLOW+"enter your range"+color.END)
# rand_range = int(input(color.BOLD +color.PURPLE+"your range is :"+color.END))
# total_nodes = []
# x = random.randint(0,150)
# y = random.randint(0,150)
# for i in range(rand_range):
#     for j in range(rand_range):
#         total_nodes.append(tuple([int(i), int(j)]))
# black_nodes = []
# for node in total_nodes[x:y]:
#     remove_node=random.choice(total_nodes)
#     black_nodes.append(remove_node)

# total_nodes = list(set(total_nodes) - set(black_nodes))

# start_node = total_nodes[0]
# target_node = total_nodes[120]
# fiiled_nodes = arr = total_nodes


fiiled_nodes = arr 

# find Neighborhood
frontier = []
for node in arr:
    x = int(node[0])
    y = int(node[1])
    right = tuple([x, y+1])
    left = tuple([x, y-1])
    up = tuple([x-1, y])
    down = tuple([x+1, y])
    frontier.append([up, right, down, left])
    for node in frontier:
        for i in node:
            # chek the condition
            if i[0] < 0 or i[1] < 0 or i[0] > board_limited or i[1] > board_limited or i not in fiiled_nodes:
                node.remove((i))
# convert to string type for adding to graph
frontier_string_type = []
for i in frontier:
    frontier_test = []
    for j in i:
        frontier_test.append((str(j)))
    frontier_string_type.append(frontier_test)


frontier_int_type = []
for i in frontier:
    frontier_int_test = []
    for j in i:
        frontier_int_test.append((j))
    frontier_int_type.append(frontier_int_test)

frontier_string_type_A_star = []
for i in frontier:
    frontier_test = []
    for j in i:
        frontier_test.append(([str(j)]))
    frontier_string_type_A_star.append(frontier_test)

graph = {}
index = 0
index_1 = 0
index_2 = 0
graph_test = {}
graph_A = {}


# graph for ids
for i in arr:
    graph_test[str(i)] = frontier_string_type[index_1]
    index_1 += 1
visited = []
for j in graph_test:
    visited.append(j)
    for k in graph_test[j]:
        if k in visited:
            graph_test[j].remove(k)

# graph for bfs
for i in arr:
    graph[str(i)] = set(frontier_string_type[index])
    index += 1

# graph for A*
for i in arr:
    graph_A[str(i)] = frontier_string_type_A_star[index_2]
    index_2 += 1


# bfs algorithm
def bfs(graph, start_node,end_node):
    if start_node == end_node:
        print([start_node])
        return

    queue = deque([start_node])
    parent = {}
    parent[start_node] = start_node

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor == end_node:
                parent[neighbor] = current
                path(parent, neighbor, start_node)
                return
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    print(color.BOLD +color.WARNING+color.UNDERLINE+"BFS Algorithm Reasult : "+color.END)
    print(color.BOLD +color.WARNING+"No path found"+color.END)


def path(parent, end_node, start_node):
    path = [end_node]
    while end_node != start_node:
        end_node = parent[end_node]
        path.insert(0, end_node)
    print(color.BOLD +color.WARNING+color.UNDERLINE+"BFS Algorithm Reasult : "+color.END)
    print(color.BOLD +color.WARNING+" path in" +color.RED+ "BFS" +color.WARNING+" algorithm is:"+color.RED+" {} ".format(path)+ color.END)
    print(color.BOLD +color.WARNING+"lenth of the path in BFS algorithm:"+color.RED+ "{}".format(len(path))+color.WARNING+"nodes"+ color.END)

bfs(graph, str(start_node), str(target_node))


# IDS algorithm


def DFS(start_node , target_node, graph_test , max_depth):
    print(start_node)
    if start_node==str(target_node):
        return True;
    if max_depth<=0:
        return False
    for node in graph_test[str(start_node)]:
        if DFS(node,target_node,graph_test,max_depth-1):
            return True;
    return False;

def IDS(start_node , target_node , graph_test , max_depth):
    for i in range(max_depth):
        print(color.BOLD +color.YELLOW+"in Limit {} :".format(i)+color.END)
        if DFS(start_node , target_node , graph_test , i):
            return True;
    return False;

print(color.BOLD +color.WARNING+color.UNDERLINE+"IDS Algorithm Reasult : "+color.END)

if not IDS(start_node,target_node,graph_test, limit):

    print("Algorithm is not responsive in the input Limit")
else:
    print(color.BOLD +color.GREEN+"IDS Algorithm is responsive in the input Limit"+color.END)


x_start = start_node[0]
y_start = start_node[1]
x_target = target_node[0]
y_target = target_node[1]


# mohasebe g

for parent in graph_A:
    for child in graph_A[parent]:
        x = int(child[0][1])
        y = int(child[0][4])
        g = abs(x_start - x) + abs(y_start - y)
        child.append(g)

# mohasebe h

heuristic = {}
for parent in graph_A:
    x_parent = int(parent[1])
    y_parent = int(parent[4])
    h = abs(x_target - x_parent) + abs(y_target - y_parent)
    heuristic[parent] = h

cost = {str(start_node): 0}

heuristic_start_node = abs(x_target - x_start) + abs(y_target - y_start)


# A* algorithm
def A_Search():
    global graph_A, heuristic
    closed = []
    opened = [[str(start_node), heuristic_start_node]]

    while True:
        f = [i[1] for i in opened]
        chosen_index = f.index(min(f))
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == str(target_node):
            break
        for item in graph_A[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp = [item[0], fn_node]
            opened.append(temp)

    node_t = str(target_node)
    sequence = [str(target_node)]
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]
        if node_t in [children[0] for children in graph_A[check_node]]:
            children_costs = [temp[1] for temp in graph_A[check_node]]
            children_nodes = [temp[0] for temp in graph_A[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(node_t)] == cost[node_t]:
                sequence.append(check_node)
                node_t = check_node
    sequence.reverse()

    return closed, sequence


visited_nodes, optimal_nodes = A_Search()
print(color.BOLD +color.WARNING+color.UNDERLINE+"A* Algorithm Reasult : "+color.END)
print(color.BOLD +color.GREEN+'Traveled Nodes: '+color.END +color.BLUE+ str(visited_nodes)+color.END)
print(color.BOLD +color.GREEN+'Proposed path of Algorithm A*: '+color.END+color.YELLOW+str(optimal_nodes)+color.END)



