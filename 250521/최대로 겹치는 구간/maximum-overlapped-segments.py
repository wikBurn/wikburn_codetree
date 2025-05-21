MAX_R=200
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

array=[0]*(MAX_R+1)
for x1,x2 in segments:
    x1,x2= abs(x1), abs(x2)
    for i in range(x1,x2):
        array[i]+=1

res = max(array)
print(res)