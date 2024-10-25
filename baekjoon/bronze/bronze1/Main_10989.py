# Bronze I _ 10989번 _ 수 정렬하기 3

import sys

if __name__ == '__main__':
    N = int(input())
    nums = []

    for _ in range(N):
        nums.append(int(input()))

    nums.sort()
    for n in nums:
        print(n)