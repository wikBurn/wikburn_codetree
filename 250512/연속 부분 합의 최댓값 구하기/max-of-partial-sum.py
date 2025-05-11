import sys

INT_MIN =  -sys.maxsize
n = int(input())
a = [0] + list(map(int, input().split()))
# dp[i]: When the position of the last element of the selected contiguous subsequence is i,
#        the maximum sum obtainable
dp = [
    0
    for _ in range(n + 1)
]


def initialize():
    for i in range(1, n + 1):
        dp[i] = INT_MIN
    dp[1] = a[1]

initialize()


for i in range (2, n+1):
    dp[i] = max(dp[i - 1] + a[i], a[i])


ans = max(dp[1:n + 1])
print(ans)