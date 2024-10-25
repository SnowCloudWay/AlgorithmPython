# Silver II _ 1406 _ 에디터

import sys
from collections import deque
input = sys.stdin.readline

# 스택 + 덱
S = list(input().strip())
dq = deque()
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == 'L' and S:
        dq.appendleft(S.pop())
    elif command[0] == 'D' and dq:
        S.append(dq.popleft())
    elif command[0] == 'B' and S:
        S.pop()
    elif command[0] == 'P':
        S.append(command[1])

sys.stdout.write(''.join(S) + ''.join(dq))

# 스택 + 스택       : 틀림, 다시 풀기
# S1 = list(input().split())
# S2 = []
# N = int(input())
#
# for _ in range(N):
#     command = input().split()
#     if command[0] == 'L' and S1:
#         S2.append(S1.pop())
#     elif command[0] == 'D' and S2:
#         S1.append(S2.pop())
#     elif command[0] == 'B' and S1:
#         S1.pop()
#     elif command[0] == 'P':
#         S1.append(command[1])
#
# sys.stdout.write(''.join(S1) + ''.join(reversed(S2)))