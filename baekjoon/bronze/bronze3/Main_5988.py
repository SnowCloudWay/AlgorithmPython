# Bronze III _ 5988 _ 홀수일까 짝수일까

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        sys.stdout.write('even\n')
    else:
        sys.stdout.write('odd\n')