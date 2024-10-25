# Silver IV _ 1920 _ 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
s = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in s:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')



# 이진탐색
# def binary_search(target, data):
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#
#     return 0
#
# if __name__ == '__main__':
#     n = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().split()))
#     m = int(sys.stdin.readline())
#     f = list(map(int, sys.stdin.readline().split()))
#
#     a.sort()
#
#     for i in f:
#         result = binary_search(i, a)
#         sys.stdout.write(str(result) + '\n')