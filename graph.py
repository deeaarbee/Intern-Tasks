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

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printyesorno(self, each):
            if each == 3 or each == 4 or each == 1:
                return 1
            else:
                return 0

    def convertToNumber(self,node):
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

    def printAllPathsUtil(self, u, d, visited, path):
        visited[u] = True
        path.append(u)
        # path.append("->")
        if u == d:
            for each in path:
                flag = self.printyesorno(each)
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
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False

    def printAllPaths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path)


totalNodes = 5
g = Graph(totalNodes)

print("enter the Number of paths:")
number = int(input())
for i in range(0,number):
    print("from_state :")
    fromState = str(input())
    print("to_state :")
    toState = str(input())
    g.addEdge(g.convertToNumber(fromState), g.convertToNumber(toState))

states = []
print("Initial State : ")
start = str(input())
print("No of Final States : ")
finals = int(input())
for each in range(0,finals):
    finalState = str(input())
    states.append(finalState)
states = [1,2,3,4]
for each in states:
    s = g.convertToNumber(start)
    d = each
    g.printAllPaths(s, d)

