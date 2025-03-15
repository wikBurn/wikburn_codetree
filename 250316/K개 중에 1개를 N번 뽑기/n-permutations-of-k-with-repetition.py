K, N = map(int, input().split())

# Please write your code here.
answer = []


def print_answer():
    for element in answer:    
        print(element, end=' ')
    print()

def choose_num(curr_number):
    #Termination
    if curr_number == N + 1:
        print_answer()
        return
    
    for i in range(1, K + 1):
        answer.append(i)
        choose_num(curr_number + 1)
        answer.pop()
    return

choose_num(1)
