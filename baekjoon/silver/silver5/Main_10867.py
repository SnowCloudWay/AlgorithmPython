# Silver V _ 10867 _ 중복 빼고 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))

sys.stdout.write(' '.join(map(str, sorted(nums))))