# Bronze IV _ 23795 _ 사장님 도박은 재미로 하셔야 합니다

import sys
input = sys.stdin.readline

totalSum = 0

while True:
    num = int(input())
    if num == -1:
        break
    totalSum += num

print(totalSum)