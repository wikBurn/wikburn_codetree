n = int(input())
visited = set()
# Please write your code here.

answer = []
def print_answer():
    for element in answer:
        print(element, end=' ')
    print()

def add_number(current_number):
    if current_number >= n + 1:
        print_answer()
        return
    
    for i in range(1, n + 1):
        if i in visited:
            continue
        visited.add(i)
        answer.append(i)
        add_number(current_number + 1)
        answer.pop()
        visited.remove(i)

add_number(1)


