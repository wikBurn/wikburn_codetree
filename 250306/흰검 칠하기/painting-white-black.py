MAX_VAL = 1000 * 100 * 2
OFFSET = 1000 * 100

array = [0] * (MAX_VAL + 1)
arrayB = [0] * (MAX_VAL + 1)
arrayW = [0] * (MAX_VAL + 1)

b, w, g = 0, 0, 0
position = OFFSET
n = int(input())

for _ in range(n):
    num, direction = tuple(input().split())
    num = int(num)
    if direction == 'R':
        while num > 0:
            array[position] = 1
            arrayB[position] += 1
            num -= 1
            if num > 0:
                position += 1
    else:
        while num > 0:
            array[position] = 2
            arrayW[position] += 1
            num -= 1
            if num > 0:
                position -= 1

for i in range(MAX_VAL + 1):
    if arrayW[i] >= 2 and arrayB[i] >= 2:
        g += 1
    elif array[i] == 1:
        b += 1
    elif array[i] == 2:
        w += 1
print(w, b, g)

# Please write your code here.