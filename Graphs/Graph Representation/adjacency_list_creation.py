num_of_vertices = 6
adj_ls = [[] for i in range(num_of_vertices)]


def create_edge(vertex_1, vertex_2, is_undirect=True):
    adj_ls[vertex_1].append(vertex_2)
    if is_undirect:
        adj_ls[vertex_2].append(vertex_1)


def display_graph():
    for i in range(len(adj_ls)):
        print(i, adj_ls[i])


create_edge(0, 1, True)
create_edge(1, 2, True)
create_edge(2, 3, True)
create_edge(3, 4, True)
create_edge(4, 5, True)
create_edge(5, 0, True)
create_edge(0, 2, True)
create_edge(1, 3, True)
create_edge(2, 4, True)
create_edge(3, 5, True)
create_edge(4, 0, True)
create_edge(5, 1, True)

display_graph()
