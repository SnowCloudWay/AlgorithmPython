# Silver V _ 11728 _ 배열 합치기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_idx, b_idx = 0, 0

# 정렬
c = a + b
c.sort()
sys.stdout.write(str(' '.join(map(str, c))))

# 투 포인터
# c = []
#
# for _ in range(n+m):
#     if n > a_idx and m > b_idx:
#         if a[a_idx] < b[b_idx]:
#             c.append(a[a_idx])
#             a_idx += 1
#         else:
#             c.append(b[b_idx])
#             b_idx += 1
#     elif n > a_idx and m <= b_idx:
#         c.append(a[a_idx])
#         a_idx += 1
#     else:
#         c.append(b[b_idx])
#         b_idx += 1
#
# sys.stdout.write(str(' '.join(map(str, c))))
