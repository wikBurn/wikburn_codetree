MAX_G = 200
OFFSET = 100
Grid = [[0] * (MAX_G+1) for _ in range(MAX_G+1)]

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+OFFSET)
    y1.append(b+OFFSET)
    x2.append(c+OFFSET)
    y2.append(d+OFFSET)

# Please write your code here.

for i in range(0,n):
    for x in range(x1[i],x2[i]):
        for y in range(y1[i],y2[i]):
            Grid[x][y]=1

res = 0
for x in range(0,MAX_G+1):
    for y in range(0,MAX_G+1):
        if Grid[x][y]==1:
            res+=1
print(res)