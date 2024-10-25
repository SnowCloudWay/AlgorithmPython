# Python Queue
from queue import Queue

# 큐 생성
q = Queue()

# 큐에 값 추가
q.put(10)
q.put(20)
q.put(30)

# 큐의 크기 출력
print("큐의 크기:", q.qsize())

# 큐의 맨 앞 원소 출력
print("맨 앞 원소:", q.queue[0])

# 큐에서 원소 제거
print("삭제 원소:", q.get())
print("삭제 후 맨 앞 원소:", q.queue[0])

# 전체 삭제
while not q.empty():
    q.get()

print("큐의 크기:", q.qsize())
