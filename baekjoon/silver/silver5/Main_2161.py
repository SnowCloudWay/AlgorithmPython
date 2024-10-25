# Silver V _ 2161 _ 카드1

import sys

# 스택
n = int(sys.stdin.readline())
card = [i for i in range(1, n+1)]
out = []

while len(card) > 1:
    out.append(card.pop(0))
    card.append(card.pop(0))

print(*out, card[0])



# 데큐
# from collections import deque
#
# n = int(sys.stdin.readline())
# dq = deque(i for i in range(1, n+1))
#
# while True:
#     if len(dq) == 1:
#         break
#     sys.stdout.write(str(dq.popleft())+' ')
#     dq.append(dq.popleft())
#
# sys.stdout.write(str(dq[0]))