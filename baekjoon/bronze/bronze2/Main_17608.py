# Bronze II _ 17608 _ 막대기

import sys

n = int(sys.stdin.readline())

stack = list(map(int, sys.stdin.read().splitlines()))
# stack = []
# for _ in range(n):
#     stack.append(int(sys.stdin.readline()))

last = stack[-1]
cnt = 1

for s in stack[::-1]:
    if s > last:
        last = s
        cnt += 1

print(cnt)