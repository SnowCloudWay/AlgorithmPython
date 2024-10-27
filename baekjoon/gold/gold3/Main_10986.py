# Gold III _ 10986 _ 나머지 합

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))


# 시간 초과
# prefix_sum = [0] * n
# prefix_sum[0] = a[0]
# for i in range(1, n):
#     prefix_sum[i] = prefix_sum[i-1] + a[i]
#
# cnt = 0

# for start in range(n):
#     for end in range(start, n):
#         if start == 0:
#             ps = prefix_sum[end]
#         else:
#             ps = prefix_sum[end] - prefix_sum[start-1]
#
#         if ps % m == 0:
#             cnt += 1
#
# sys.stdout.write(str(cnt))