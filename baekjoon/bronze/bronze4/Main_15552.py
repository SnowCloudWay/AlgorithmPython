# Bronze IV _ 15552 _ 빠른 A+B

import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(A + B)+"\n")