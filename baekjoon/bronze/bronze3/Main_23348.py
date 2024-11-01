# Bronze III _ 23348 _ 스트릿 코딩 파이터

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
n = int(input())
maxScore = 0

for _ in range(n):
    sumScore = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        sumScore += (A*a) + (B*b) + (C*c)
    maxScore = max(maxScore, sumScore)

sys.stdout.write(str(maxScore))