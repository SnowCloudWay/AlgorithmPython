# Gold IV _ 1806 _ 부분합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
intervalSum = 0
minLen = n
end = 0

for start in range(n):
    while intervalSum < s and end < n:
        intervalSum += nums[end]
        end += 1
    if intervalSum >= s:
        minLen = min(minLen, end - start)
    intervalSum -= nums[start]

sys.stdout.write(str(minLen))