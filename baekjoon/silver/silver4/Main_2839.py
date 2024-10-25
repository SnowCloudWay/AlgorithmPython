# Silver IV _ 2839번 _ 설탕 배달

# DP (BottomUp)
import sys

N = int(sys.stdin.readline().rstrip())

dp = [-1] * 5001

dp[3] = dp[5] = 1

for i in range(6, N + 1):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 1
    elif i % 3 == 0:
        dp[i] = dp[i - 3] + 1
    elif dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[N])

# import sys
#
# N = int(sys.stdin.readline().rstrip())
#
# dp = [5000] * 5001
#
# dp[3] = dp[5] = 1
#
# for i in range(6, N+1):
#     dp[i] = min(dp[i-3], dp[i-5]) + 1
#
# if dp[N] >= 5000:
#     print(-1)
# else:
#     print(dp[N])

# 그리디
# if __name__ == '__main__':
#     num = int(input())
#     count = 0
#
#     while num >= 0:
#         if num % 5 == 0:
#             count += int(num // 5)
#             print(count)
#             break
#
#         num -= 3
#         count += 1
#
#     else:
#         print(-1)