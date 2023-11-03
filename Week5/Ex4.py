# tao lop do thi
class UnirectedGraph:
    def __init__(self, N):
        self.numberOfPoints = N
        # phan tu [u][v] luu tru capacity tu u sang v
        self.edges = [[0] * N for _ in range(N)]

    # them canh
    def addEdge(self,u,v,w):
        self.edges[u][v] = w
        self.edges[v][u] = w

    def dfs(self,source):
        min = 0
        visitedPoint = [False] * self.numberOfPoints
        stack = []

        while stack:
            u = stack.pop()
            visitedPoint[u] = True

            for v, weight in enumerate(self.edges[u]):
                if not visitedPoint[v]:
                    stack.append(v)
        return 0


if __name__ == "__main__":
    x = 1
    # N, M = map(int, input().split())
    # source, target = map(int, input().split())
    # dG = DirectedGraph(N)
    # # du lieu in put cac diem duoc danh dau tu 1 den N
    # # du lieu luu trong ma tran danh dau tu 0 den N-1
    # for _ in range(M):
    #     u, v, c = map(int, input().split())
    #     #print(u, v, c)
    #     dG.addEdge(u - 1, v - 1, c)
    # print(dG.maxFlow(source - 1,target - 1))



