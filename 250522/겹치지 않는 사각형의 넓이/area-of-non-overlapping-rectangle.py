OFFSET = 1000
MAX_G=2000

n = 3
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

Grid = [[0] * (MAX_G+1) for _ in range(MAX_G+1)]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            Grid[x][y] = i

area = 0
for x in range(0,MAX_G):
    for y in range(0,MAX_G):
        if Grid[x][y]==1 or Grid[x][y]==2:
            area+=1

print(area)















