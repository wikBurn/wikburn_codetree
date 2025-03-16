n = int(input())

# Please write your code here

answer = []
used = set()

def print_answer():
    for element in answer:
        print(element, end=' ')
    print()

def append_number(current_number):

    if current_number >= n + 1:
        print_answer()
        return
    for i in range(n, 0, -1):
        if i in used:
            continue
        used.add(i)
        answer.append(i)
        append_number(current_number + 1)
        answer.pop()
        used.remove(i)
    return

append_number(1)