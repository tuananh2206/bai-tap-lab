def build_graph_representations(num_nodes, edges):
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    adj_list = {i: [] for i in range(num_nodes)}

    for u, v in edges:
        if not (0 <= u < num_nodes and 0 <= v < num_nodes):
            raise ValueError(f"Canh ({u}, {v}) khong hop le.")

        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_matrix, adj_list


if __name__ == "__main__":
    num_nodes = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

    matrix, adj_list = build_graph_representations(num_nodes, edges)

    print("Ma tran ke:")
    for row in matrix:
        print(row)

    print("\nDanh sach ke:")
    print(adj_list)