from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:

            # print(neighbour,end= " ")
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


    def printyesorno(self, each):
            if each == 3 or each == 4:
                return 1
            else:
                return 0

    def convertnumber(self,path):
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
            return path

    def printAllPathsUtil(self, u, d, visited, path):
        visited[u] = True
        path.append(u)
        # path.append("->")


        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            for each in path:
                print(each)
                flag = self.printyesorno(each)
                if each == 2 and path[each+1]== 1:
                    print("loop")

            # if flag == 0:
            #     for n, i in enumerate(path):
            #         if i == 0:
            #             path[n] = "NEW"
            #         if i == 1:
            #             path[n] = "ENGAGED"
            #         if i == 2:
            #             path[n] = "SUSPENDED"
            #         if i == 3:
            #             path[n] = "TERMINATED"
            #         if i == 4:
            #             path[n] = "COMPLETED"
            #     print(path,end=" ")
            #     print("no")
            # else:
            #     for n, i in enumerate(path):
            #         if i == 0:
            #             path[n] = "NEW"
            #         if i == 1:
            #             path[n] = "ENGAGED"
            #         if i == 2:
            #             path[n] = "SUSPENDED"
            #         if i == 3:
            #             path[n] = "TERMINATED"
            #         if i == 4:
            #             path[n] = "COMPLETED"
            #     print(path, end=" ")
            #     print("yes")

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

    # def printpaths(self, rec):
    #     x=0
    #     for each in rec:
    #         print(each)
    #     return



g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(1, 3)
g.addEdge(1, 4)

states = [1,2,3,4]
# for each in states:
#     s = 0
#     d = each
g.printAllPaths(0, 4)

print("\n")
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

