from collections import defaultdict


# 0 - NEW - INITIAL STATE
# 1 - ENGAGED - MIDDLE
# 2 - SUSPENDED - MIDDLE
# 3 - TERMINATED - FINAL
# 4 - COMPLETED - FINAL


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict([])

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_yes_or_no(self, node):
            if node == 3 or node == 4 or node == 1:
                return 1
            else:
                return 0

    def convert_to_number(self,node):
        path = 0
        if node == "NEW":
            path = 0
        if node == "ENGAGED":
            path = 1
        if node == "SUSPENDED":
            path = 2
        if node == "TERMINATED":
            path = 3
        if node == "COMPLETED":
            path = 4
        return path

    def print_all_paths_util(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            for each in path:
                flag = self.print_yes_or_no(each)
            if flag == 0:
                for n, i in enumerate(path):
                    if i == 0:
                        path[n] = "NEW"
                    if i == 1:
                        path[n] = "ENGAGED"
                    if i == 2:
                        path[n] = "SUSPENDED"
                    if i == 3:
                        path[n] = "TERMINATED"
                    if i == 4:
                        path[n] = "COMPLETED"
                print(path,end=" ")
                print("Not Possible")
            else:
                for n, i in enumerate(path):
                    if i == 0:
                        path[n] = "NEW"
                    if i == 1:
                        path[n] = "ENGAGED"
                    if i == 2:
                        path[n] = "SUSPENDED"
                    if i == 3:
                        path[n] = "TERMINATED"
                    if i == 4:
                        path[n] = "COMPLETED"
                print(path, end=" ")
                print("Possible")

        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.print_all_paths_util(i, d, visited, path)
        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.print_all_paths_util(s, d, visited, path)


totalNodes = 5
g = Graph(totalNodes)

print("enter the Number of paths:")
number = int(input())
for i in range(0,number):
    print("from_state :")
    fromState = str(input())
    print("to_state :")
    toState = str(input())
    g.add_edge(g.convert_to_number(fromState), g.convert_to_number(toState))

states = []
print("Initial State : ")
start = str(input())
print("No of Final States : ")
finals = int(input())
for each in range(0,finals):
    finalState = str(input())
    states.append(finalState)
states = [1, 2, 3, 4]
for each in states:
    s = g.convert_to_number(start)
    d = muach
    g.print_all_paths(s, d)

