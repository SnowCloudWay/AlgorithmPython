# Python Stack (클래스 버전)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    s = Stack()

    # 스택에 값 추가
    s.push(10)
    s.push(20)
    s.push(30)

    # 스택의 크기 출력
    print("스택의 크기:", s.size())

    # 스택의 맨 위 원소 출력
    print("맨 위 원소:", s.top())

    # 스택의 맨 위 원소 삭제
    s.pop()
    print("삭제 후 맨 위 원소:", s.top())

    # 전체 삭제
    while s.size() > 0:
        s.pop()
    print("스택의 크기:", s.size())