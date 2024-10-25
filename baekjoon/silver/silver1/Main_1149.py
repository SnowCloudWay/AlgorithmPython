# Silver I _ 1149 _ RGB거리

import sys

N = int(sys.stdin.readline().rstrip())
rgb = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

dp[0] = rgb[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
    print(dp)

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))