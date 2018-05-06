from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    @staticmethod
    def print_yes_or_no(node):
            if node == 3 or node == 4 or node == 1:
                return 1
            else:
                return 0

    def print_all_paths_util(self, u, d, visited, path):

        visited[u] = True
        path.append(u)

        if u == d:
            check=0
            for each in path:
                check = self.print_yes_or_no(each)
            if check == 0:
                print(path, end=" ")
                print("Not Possible")
            else:
                print(path, end=" ")
                print("Possible")

        else:
            for i in self.graph[u]:
                if visited[i] is False:
                    self.print_all_paths_util(i, d, visited, path)

        path.pop()
        visited[u] = False

    def print_paths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.print_all_paths_util(s, d, visited, path)


def get_inputs():
    graph = Graph(5)
    print("enter the Number of paths:")
    number = int(input())
    for i in range(0, number):
        print("from_state :")
        fromState = int(input())
        print("to_state :")
        toState = int(input())
        graph.add_edge(fromState, toState)

    states = []
    print("Initial State : ")
    start = input()
    print("No of Final States : ")
    finals = int(input())
    for each in range(0, finals):
        finalState = int(input())
        states.append(finalState)
    return graph


def print_all_paths(graphObject):
    states = [1, 2, 3, 4]
    for each in states:
        s = 0
        d = each
        graphObject.print_paths(s, d)
    return


g = get_inputs()
print_all_paths(g)




