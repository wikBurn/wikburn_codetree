n, m = map(int, input().split())
#edges = [tuple(map(int, input().split())) for _ in range(m)]
# Please write your code here.
def create_graph(n, m):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        i, j = tuple(map(int, input().split()))
        graph[i][j] = 1
        graph[j][i] = 1
    return graph

graph = create_graph(n, m)
#print(graph)
answer = 0
visited = [False] * (n + 1)
def dfs(current):
    global answer
    answer += 1
    visited[current] = True
    #print(current)
    for nxt in range(1, n + 1):
        #print(next)
        if graph[current][nxt] and not visited[nxt]:
            dfs(nxt)
dfs(1)

print(answer - 1)