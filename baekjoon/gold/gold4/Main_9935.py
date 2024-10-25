# Gold IV _ 9935번 _ 문자열 폭발

import sys

if __name__ == '__main__':
    a = sys.stdin.readline().rstrip()
    b = list(sys.stdin.readline().rstrip())
    n = len(b)
    s = []

    for i in a:
        s.append(i)
        if s[-n:] == b:
            for _ in range(n):
                s.pop()

    if s:
        print(''.join(s))
    else:
        print('FRULA')