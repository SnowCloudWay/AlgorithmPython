# Python Stack (그냥 리스트 버전)
# 스택 생성
s = []

# 스택에 값 추가
s.append(10)
s.append(20)
s.append(30)

# 스택의 크기 출력
print("스택의 크기:", len(s))

# 스택의 맨 위 원소 출력
print("맨 위 원소:", s[-1])

# 스택의 맨 위 원소 원소 삭제
s.pop()
print("삭제 후 맨 위 원소,", s[-1])

# 전체 삭제 : 빈 스택에서 pop하거나 s[-1]하면 실행오류!
while len(s) > 0:
    s.pop()
print("스택의 크기", len(s))
