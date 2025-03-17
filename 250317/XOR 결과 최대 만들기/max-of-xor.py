n, m = map(int, input().split())
A = list(map(int, input().split()))

answer = []
result = 0

def check(answer):
    global result  # Declare that we're using the global 'result'
    value = 0
    for num in answer:
        value ^= num  # Perform XOR for each number in 'answer'
    result = max(result, value)

def choose_number(current_index):
    # If we've selected m numbers, check the result
    if len(answer) == m:
        #print(answer)
        check(answer)
        return
    # Iterate over remaining numbers starting from current_index
    for i in range(current_index, n):
        answer.append(A[i])
        choose_number(i + 1)  # Use i+1 to avoid reusing the same element
        answer.pop()
    
choose_number(0)
print(result)
