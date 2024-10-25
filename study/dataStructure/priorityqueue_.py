# 우선순위 큐

from queue import PriorityQueue

# 우선순위 큐 생성
que = PriorityQueue()
# que = PriorityQueue(maxsize=5)    # 우선순위 큐 크기 설정 가능

# 원소 추가
que.put(4)
que.put(1)
que.put(7)
que.put(3)

# 원소 삭제
# que.get()
print(que.get())
print(que.get())
print(que.get())
print(que.get())

# 우선순위 원소 추가
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))
print(que.get()[1])
print(que.get()[1])
print(que.get()[1])

# 크기 확인
print(que.qsize())

# 비었는지 확인
print(que.empty())

# 가득 찼는지 확인
print(que.full())