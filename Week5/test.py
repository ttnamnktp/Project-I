def is_hamiltonian(graph):
    n = graph['n']
    m = len(graph['edges'])

    if n < 3:
        return 0  # Đồ thị không đủ số đỉnh

    if m < n - 1:
        return 0  # Đồ thị không đủ cạnh

    def dfs(node, visited, remaining):
        if remaining == 0:
            return 1  # Tìm thấy chu trình Hamilton

        visited[node] = True
        for neighbor in graph['adjacency_list'][node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, remaining - 1):
                    return 1

        visited[node] = False
        return 0

    visited = [False] * (n + 1)
    for start_node in range(1, n + 1):
        if dfs(start_node, visited, n - 1):
            return 1

    return 0


# Input và kiểm tra từng đồ thị
T = int(input())
results = []

for _ in range(T):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    adjacency_list = [[] for _ in range(n + 1)]

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    graph = {'n': n, 'edges': edges, 'adjacency_list': adjacency_list}
    result = is_hamiltonian(graph)
    results.append(result)

# Output
for result in results:
    print(result)
