# Bronze II _ 22966 _ 가장 쉬운 문제를 찾는 문제

import sys
input = sys.stdin.readline

d = dict()
n = int(input())

for _ in range(n):
    a, b = input().strip().split()
    d[int(b)] = a

s_d = sorted(d.items())

print(s_d[0][1])