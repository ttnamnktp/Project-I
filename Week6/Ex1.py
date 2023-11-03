# tao lop do thi
class DirectedGraph:
    def __init__(self, N):
        self.numberOfPoints = N
        # phan tu [u][v] luu tru capacity tu u sang v
        self.edges = [[0] * N for _ in range(N)]

    # them canh
    def addEdge(self,u,v,c):
        self.edges[u][v] = c

    def dfs(self,source,target,parent):
        visitedPoint = [False] * self.numberOfPoints
        stack = [(source,float("inf"))]

        while stack:
            u, minCapacity = stack.pop()
            visitedPoint[u] = True

            for v,newCapacity in enumerate(self.edges[u]):
                if not visitedPoint[v] and newCapacity > 0:
                    minCapacity = min(minCapacity,newCapacity)
                    parent[v] = u
                    if v == target:
                        return minCapacity
                    stack.append((v,newCapacity))
        return 0

    def maxFlow(self,source,target):
        parent = [-1] * self.numberOfPoints
        max_flow = 0

        while True:
            minCapacity = self.dfs(source,target,parent)
            if minCapacity == 0:
                break
            max_flow += minCapacity

            v = target
            while v != source:
                u = parent[v]
                self.edges[u][v] -= minCapacity
                self.edges[v][u] += minCapacity
                v = u
        return max_flow

if __name__ == "__main__":
    N, M = map(int, input().split())
    source, target = map(int, input().split())
    dG = DirectedGraph(N)
    # du lieu in put cac diem duoc danh dau tu 1 den N
    # du lieu luu trong ma tran danh dau tu 0 den N-1
    for _ in range(M):
        u, v, c = map(int, input().split())
        #print(u, v, c)
        dG.addEdge(u - 1, v - 1, c)
    print(dG.maxFlow(source - 1,target - 1))



