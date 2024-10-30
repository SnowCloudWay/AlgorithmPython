# Bronze III _ 4458 _ 첫 글자를 대문자로

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    sys.stdout.write(s[:1].upper() + s[1:]+'\n')
