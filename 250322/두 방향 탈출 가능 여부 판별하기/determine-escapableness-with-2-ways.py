n, m = map(int, input().split())
#grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def create_graph(n):
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    return graph

graph = create_graph(n)
visited = [[False] * m for _ in range(n)]
def can_go(x, y):
    global graph
    if x < 0 or x > (m - 1) or y < 0 or y > (n - 1):
        return False
    if visited[x][y] == True or graph[x][y] == 0:
        return False
    return True
answer = 0
def dfs(x, y):
    global answer
    if (x, y) == (n - 1, m - 1):
        answer = 1
    dxs, dys = [1, 0], [0, 1]
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            dfs(new_x, new_y)

value = dfs(0, 0)
print(answer)