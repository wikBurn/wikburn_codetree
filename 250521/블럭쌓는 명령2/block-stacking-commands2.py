n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
array = [0]*n

for command in commands:
    start=command[0]-1
    stop=command[1]-1
    for i in range(start,stop+1):
        array[i]+=1
print(max(array))