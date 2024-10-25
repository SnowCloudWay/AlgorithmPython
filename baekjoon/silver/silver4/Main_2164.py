# Silver IV _ 2164 _ 카드2

# 데크
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
deq = deque(i+1 for i in range(N))

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    deq.popleft()
    deq.append(deq.popleft())

# 큐
# import sys
# from queue import Queue
#
# N = int(sys.stdin.readline().rstrip())
# que = Queue()
#
# for i in range(N):
#     que.put(i+1)
#
# while True:
#     if que.qsize() == 1:
#         print(que.get())
#         break
#     que.get()
#     que.put(que.get())