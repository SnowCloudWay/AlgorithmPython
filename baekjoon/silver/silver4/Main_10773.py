# Silver IV _ 10773번 _ 제로

import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline().rstrip())
    s = []
    for _ in range(K):
        num = int(sys.stdin.readline().rstrip())
        if num == 0:
            s.pop()
        else:
            s.append(num)
    print(sum(s))