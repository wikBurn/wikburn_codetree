a, b, c = map(int, input().split())

# Please write your code here.
start_time = 11 * 24 * 60 + 11 * 60 + 11
end_time = a * 24 * 60 + b * 60 + c
print(end_time - start_time if start_time <= end_time else -1)
