# Bronze III _ 9713 _ Sum of Odd Sequence

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    result = 0
    for i in range(1, int(input()) + 1):
        if i % 2 != 0:
            result += i
    sys.stdout.write(str(result)+'\n')