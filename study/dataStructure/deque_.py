from collections import deque

# 데크 생성
dq = deque()

# 데크에 값 추가
dq.append(10)       # 뒤에 추가
dq.appendleft(20)   # 앞에 추가
dq.append(30)
dq.appendleft(40)

# 데크의 크기 출력
print("데크의 크기:", len(dq))

# 데크에 있는 전체 원소 출력
print("데크의 원소:", list(dq))

# 데크의 첫 번째와 마지막 원소 출력
print("첫 번째 원소:", dq[0])
print("마지막 원소:", dq[-1])

# 데크에서 원소 제거
dq.pop()        # 뒤에서 제거
dq.popleft()    # 앞에서 제거

# 제거 후 데크의 크기와 원소 출력
print("제거 후 데크의 크기:", len(dq))
print("제거 후 데크의 원소:", list(dq))
