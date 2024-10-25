# Bronze I _ 2755 _ 이번학기 평점은 몇점?

# 파이썬의 round() 반올림은 사사오입 원칙을 따름
# 사사오입 원칙 : 반올림 대상의 값이 5일 때 앞자리 숫자가 홀수면 올림, 짝수면 내림

import sys, decimal
input = sys.stdin.readline
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

d = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7,
     'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
totalGrade = 0
totalScore = 0

n = int(input())
for _ in range(n):
    info = list(map(str, input().strip().split()))
    totalGrade += int(info[1])
    totalScore += int(info[1]) * d[info[2]]
avgScore = round(decimal.Decimal(str(totalScore / totalGrade)), 2)

sys.stdout.write(str(avgScore))