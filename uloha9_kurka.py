from collections import defaultdict, deque


def create_graph():
    """ biketrails z data.txt """
    return {
        1: [(2, 5), (3, 4), (4, 5), (5, 6)],
        2: [(6, 1), (7, 2)],
        3: [(7, 6)],
        4: [(7, 5), (8, 5)],
        5: [(8, 7), (9, 3)],
        6: [(10, 2), (11, 4)],
        7: [(10, 3), (11, 5)],
        8: [(11, 2)],
        9: [(12, 4)],
        10: [(11, 4), (12, 5)],
        11: [(12, 1)],
        12: []
    }


def calculate_in_degrees(graph):
    """vypocitaj stupne vstupnych hran pre kazdy vrchol grafu"""
    in_degree = defaultdict(int) # nemusim checkovat potom existenciu klucov

    for node in graph:
        for neighbor, _ in graph[node]:
            in_degree[neighbor] += 1
    return in_degree


def topological_sort(graph):
    in_degree = calculate_in_degrees(graph)

    # do fronty daj vsetkych co nemaju vstupne hrany
    queue = deque([node for node in graph if in_degree[node] == 0])

    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


def find_longest_path(graph, start, end):
    topo_order = topological_sort(graph)

    dist = {node: float('-inf') for node in graph}
    dist[start] = 0

    # definicia CPM algoritmu z prednasky
    for node in topo_order:
        if dist[node] != float('-inf'):
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight

    return dist[end]


def main():
    graph = create_graph()
    start = 1
    end = 12

    longest_path_length = find_longest_path(graph, start, end)
    print(f"Najdlhšia súvislá trasa má dĺžku: {longest_path_length}")


if __name__ == "__main__":
    main()