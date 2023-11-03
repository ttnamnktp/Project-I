#PYTHON
# tao lop do thi
class UndirectedGraph:
    def __init__(self, N):
        self.numberOfPoints = N
        # phan tu canh luu tru trong tu dien
        self.graph = {i : [] for i in range(1, N+1)}

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def lexicalOrderEdgeSort(self):
        for i in range(1, self.numberOfPoints+1):
            self.graph[i] = sorted(self.graph[i])

    def bfs(self):
        visitedPoints = [False] * (self.numberOfPoints + 1)
        queue = [1]
        visitedPoints[1] = True
        visitedList = []

        while True:
            #break condition
            if len(visitedList) == self.numberOfPoints:
                break

            currentPoint = queue.pop(0)
            visitedList.append(currentPoint)

            for nextPoint in self.graph[currentPoint]:
                if not visitedPoints[nextPoint]:
                    queue.append(nextPoint)
                    visitedPoints[nextPoint] = True

            if not queue:
                nextPoint = 0
                for i in range(1, self.numberOfPoints + 1):
                    if visitedPoints[i] is False:
                        nextPoint = i
                        break
                queue.append(nextPoint)
                visitedPoints[nextPoint] = True

        return visitedList


if __name__ == "__main__":
    N, M = map(int, input().split())
    uG = UndirectedGraph(N)
    for _ in range(M):
         u, v = map(int, input().split())
         uG.addEdge(u, v)
    uG.lexicalOrderEdgeSort()
    for point in uG.bfs():
         print(point, end=' ')
