def dfs_traversal(adj_list, start_node):
    if start_node not in adj_list:
        raise ValueError("Dinh bat dau khong ton tai.")

    visited = set()
    traversal_order = []

    def dfs(u):
        visited.add(u)
        traversal_order.append(u)

        for v in adj_list[u]:
            if v not in visited:
                dfs(v)

    dfs(start_node)
    return traversal_order


def has_cycle_undirected(adj_list, num_nodes):
    visited = set()

    def dfs(u, parent):
        visited.add(u)

        for v in adj_list.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True

        return False

    for node in range(num_nodes):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


if __name__ == "__main__":
    graph_with_cycle = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: []
    }

    graph_tree = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    print("Thu tu duyet DFS:",
          dfs_traversal(graph_with_cycle, 0))

    print("Do thi co chu trinh:",
          has_cycle_undirected(graph_with_cycle, 4))

    print("Do thi dang cay co chu trinh:",
          has_cycle_undirected(graph_tree, 4))