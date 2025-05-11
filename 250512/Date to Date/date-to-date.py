m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
def num_of_days(m,d):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    sum_of_days = 0
    
    for i in range(1,m):
        sum_of_days+=days[i]
    sum_of_days+=d

    return sum_of_days

ans=abs(num_of_days(m2,d2)-num_of_days(m1,d1)+1)
print(ans)
