# Silver III _ 2559 _ 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
intervalSumList = [sum(nums[:k])]

for i in range(n - k):
    intervalSum = intervalSumList[i] - nums[i] + nums[i+k]
    intervalSumList.append(intervalSum)

sys.stdout.write(str(max(intervalSumList)))


# 시간 초과
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))
# maxSum = 0
#
# for start in range(n):
#     end = start
#     totalSum = 0
#     while end < start + k:
#         if end >= n:
#             break
#         totalSum += nums[end]
#         end += 1
#         if totalSum > maxSum:
#             maxSum = totalSum
#
# sys.stdout.write(str(maxSum))