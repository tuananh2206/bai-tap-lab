from collections import deque


def count_and_find_components(adj_list, num_nodes):
    visited = set()
    components = []

    for node in range(num_nodes):
        if node in visited:
            continue

        component = []
        queue = deque([node])
        visited.add(node)

        while queue:
            u = queue.popleft()
            component.append(u)

            for v in adj_list.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        components.append(component)

    return len(components), components


if __name__ == "__main__":
    discrete_graph = {
        0: [1],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3]
    }

    count, components = count_and_find_components(
        discrete_graph, 5
    )

    print("So thanh phan lien thong:", count)
    print("Danh sach cac cum:", components)