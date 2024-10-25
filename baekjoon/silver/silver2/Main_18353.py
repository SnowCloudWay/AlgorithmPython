# Silver II _ 18353 _ 병사 배치하기

# 1. DP
import sys

n = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))


# 2. 연결리스트
# 3.