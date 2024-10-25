# Silver V _ 2751번 _ 수 정렬하기 2

import sys
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline()))
    for i in sorted(a):
        print(i)