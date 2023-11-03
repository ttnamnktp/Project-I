# Hàm tính khoảng cách ngắn nhất giữa tất cả các cặp đỉnh
def floyd_warshall(n, edges):
    # Khởi tạo ma trận khoảng cách với giá trị vô cùng
    dist = [[float('inf')] * n for _ in range(n)]

    # Đặt khoảng cách cho các cạnh trực tiếp
    for u, v, w in edges:
        dist[u - 1][v - 1] = w

    # Đặt các phần tử trên đường chéo chính thành 0
    for i in range(n):
        dist[i][i] = 0

    # Tính toán khoảng cách ngắn nhất sử dụng thuật toán Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Đọc dữ liệu vào
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Tính toán khoảng cách ngắn nhất
result = floyd_warshall(n, edges)

# In kết quả
for row in result:
    print(" ".join(map(str, row)))
