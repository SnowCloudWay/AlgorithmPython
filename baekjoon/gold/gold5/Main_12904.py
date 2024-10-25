# Gold V _ 12904 _ A와 B

# 문제는 s를 t로 바꾸기
# 밑 코드는 t를 s로 만들기

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

while True:
    if len(t) < len(s):
        sys.stdout.write('0')
        break
    elif s == t:
        sys.stdout.write('1')
        break
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
