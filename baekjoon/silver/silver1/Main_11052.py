# Silver I _ 11052 _ 카드 구매하기

# 점화식 : dp[i] = dp[i-j] + p[j]

# dp[1] = p[1]
# dp[2] = dp[1] + p[1] or dp[0] + p[2]
# dp[3] = dp[2] + p[1] or dp[1] + p[2] or dp[0] + p[3]
# dp[4] = dp[3] + p[1] or dp[2] + p[2] or dp[1] + p[3] or dp[0] + p[4]

import sys

N = int(sys.stdin.readline().rstrip())
P = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * (N + 1)

for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + P[j]:
            dp[i] = dp[i-j] + P[j]
        # dp[i] = max(dp[i], P[j] + dp[i-j])

sys.stdout.write(str(dp[N]))

# Java
# Math.max(dp[j] + dp[i-j], dp[i])