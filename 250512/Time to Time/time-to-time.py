a, b, c, d = map(int, input().split())

# Please write your code here.
MinToAB=(a*60)+b
MinTOCD=(c*60)+d

timePassed=abs(MinTOCD-MinToAB)
print(timePassed)