K, N = map(int, input().split())

# Please write your code here.
answer = []

def print_answer():
    for element in answer:
        print(element, end=' ')
    print()

def choose_number(current_number):
    if current_number == N + 1:
        print_answer()
        return
    
    for i in range(1, K + 1):
        if current_number >= 3 and answer[-1] == i and answer[-2] == i:
            continue
        answer.append(i)
        choose_number(current_number + 1)
        answer.pop()
    return

choose_number(1)