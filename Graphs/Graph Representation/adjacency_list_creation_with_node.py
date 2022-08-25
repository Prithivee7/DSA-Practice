class Graph:
    def __init__(self, adjacency_list) -> None:
        self.adjacency_list = adjacency_list

    def graph_status(self):
        print(self.adjacency_list)

    def add(self, edge):
        pass


class Edge:

    pass


graph = Graph([])
graph.add([1, 2])
graph.add([2, 3])
graph.add([3, 4])
graph.add([1, 4])
graph.add([1, 3])
graph.print_list()
