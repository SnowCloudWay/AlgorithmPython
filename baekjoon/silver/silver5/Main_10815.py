# Silver V _ 10815 _ 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
s = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in s:
        print(1, end=' ')
    else:
        print(0, end=' ')