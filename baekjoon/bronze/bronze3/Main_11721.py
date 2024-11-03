# Bronze III _ 11721 _ 열 개씩 끊어 출력하기

import sys
input = sys.stdin.readline

s = input().strip()

for i in range(len(s)):
    sys.stdout.write(s[i])
    if (i+1) % 10 == 0:
        sys.stdout.write('\n')
