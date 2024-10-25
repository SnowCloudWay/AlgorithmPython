# Python Queue (리스트 버전)
# 큐 생성
queue = []

# 값 추가
queue.append(10)
queue.append(20)
queue.append(30)

# 큐의 크기 출력
print("큐의 크기:", len(queue))

# 큐의 맨 앞 원소 출력
print("맨 앞 원소:", queue[0])

# 큐에서 원소 제거 : O(n)
print("삭제 원소:", queue.pop(0))
print("삭제 후 맨 앞 원소:", queue[0])

# 전체 삭제
queue.clear()
print("큐의 크기:", len(queue))
