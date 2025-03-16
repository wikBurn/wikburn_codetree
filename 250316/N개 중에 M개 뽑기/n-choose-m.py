N, M = map(int, input().split())

# Please write your code here.
answer = []

def print_answer():
    for element in answer:
        print(element, end=' ')
    print()
    return

def append_number(current_number, counter):
    #termination
    if current_number == N + 1:
        if counter == M:
            print_answer()
        return
    #nested functions
    answer.append(current_number)
    append_number(current_number + 1, counter + 1)
    answer.pop()

    append_number(current_number + 1, counter)
    return

append_number(1, 0)
