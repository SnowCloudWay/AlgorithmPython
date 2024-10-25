# Gold III _ 1644 _ 소수의 연속합

import sys
input = sys.stdin.readline

n = int(input())
primeNums = []
intervalSum = 0
end = 0
cnt = 0

for i in range(2, n+1):
    is_prime = 1
    for j in range(2, i):
        if i % j == 0:
            is_prime = 0
            break
    if is_prime == 1:
        primeNums.append(i)

primeNumsLen = len(primeNums)
for start in range(primeNumsLen):
    while intervalSum < n and end < primeNumsLen:
        intervalSum += primeNums[end]
        end += 1
    if intervalSum == n:
        cnt += 1
    intervalSum -= primeNums[start]

sys.stdout.write(str(cnt))