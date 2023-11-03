def dfs(graph, visitedPoint, startPoint, listDFS):
    visitedPoint[startPoint] = True
    listDFS.append(startPoint)
    for newPoint in sorted(graph[startPoint]):
        if not visitedPoint[newPoint]:
            dfs(graph, visitedPoint, newPoint, listDFS)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = {i:[] for i in range(1,N+1) }

    for _ in range(M):
         u, v = map(int, input().split())
         graph[u].append(v)
         graph[v].append(u)

    #khoi tao cac tham so
    visitedPoint = [False] * (N+1)
    listDFS = []
    dfs(graph, visitedPoint, 1,listDFS )
    for _ in listDFS:
        print(_,end=' ')



