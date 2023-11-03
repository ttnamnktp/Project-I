import heapq

# Hàm để tìm trọng số của cây khung nhỏ nhất bằng thuật toán Prim
def prim(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    visited = [False] * n
    min_heap = [(0, 0)]  # (trọng số, nút)
    mst_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if not visited[node]:
            mst_weight += weight
            visited[node] = True
            for neighbor, edge_weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst_weight

# Đọc dữ liệu vào
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Tìm trọng số của cây khung nhỏ nhất
result = prim(n, edges)
print(result)
