# Silver IV _ 17219 _ 비밀번호 찾기

import sys

n, m = map(int, sys.stdin.readline().split())
d = {}

for _ in range(n):
    pw = list(map(str, sys.stdin.readline().rstrip().split()))
    d[pw[0]] = pw[1]

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    sys.stdout.write(d[site] + '\n')