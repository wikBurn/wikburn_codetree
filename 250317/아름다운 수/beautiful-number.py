n = int(input())

# Please write your code here.

choosed = []
res = 0

def check_numbers(nums):
    global res
    i = 0
    while i < n:
        if i + nums[i] >= n + 1:
            return
        for j in range(i, i + nums[i]):
            if nums[i] != nums[j]:
                return
        i += nums[i]
    res += 1
    #print(res)

def choose_numbers():
    if len(choosed) == n:
        #print(choosed)
        check_numbers(choosed)
        return
    
    for i in range(1, n + 1):
        choosed.append(i)
        choose_numbers()
        choosed.pop()
    return

choose_numbers()
print(res)