MAX_VAL = 2000
OFFSET = 1000

grid = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]

for i in range(2):
    x1, y1, x2, y2 = (int(i) + OFFSET for i in input().split())
    for j in range(x1, x2+1):
        for k in range(y1, y2+1):
            grid[j][k] = 1 if i == 0 else 0

maxX = 0
minX = 2000
maxY = 0
minY = 2000

for i in range(MAX_VAL + 1):
    for j in range(MAX_VAL + 1):
        if grid[i][j] == 1:
            maxX = max(maxX, i)
            minX = min(minX, i)
            maxY = max(maxY, j)
            minY = min(minY, j)
print((maxX - minX) * (maxY - minY)) 