# Gold V _ 2096 _ 내려가기

# 다른 사람 코드
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

maxDp = nums
minDp = nums

for _ in range(n-1):
    nums = list(map(int, sys.stdin.readline().split()))
    maxDp = [max(maxDp[0], maxDp[1]) + nums[0], max(maxDp[0], maxDp[1], maxDp[2]) + nums[1], max(maxDp[1], maxDp[2]) + nums[2]]
    minDp = [min(minDp[0], minDp[1]) + nums[0], min(minDp[0], minDp[1], minDp[2]) + nums[1], min(minDp[1], minDp[2]) + nums[2]]
    
    # 엄 선생님 코드
    # maxDp = [nums[0] + max(maxDp[0:2]), nums[1] + max(maxDp), nums[2] + max(maxDp[1:])]
    # minDp = [nums[0] + min(minDp[0:2]), nums[1] + min(minDp), nums[2] + min(minDp[1:])]

print(max(maxDp), min(minDp))


# 메모리 초과
# n = int(sys.stdin.readline())
# nums = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# dpMax = [[0] * 3 for _ in range(n)]
# dpMin = [[0] * 3 for _ in range(n)]
#
# dpMax[0] = dpMin[0] = nums[0]
#
# for i in range(1, n):
#     dpMax[i][0] = max(dpMax[i - 1][0] + nums[i][0], dpMax[i - 1][0] + nums[i][1])
#     dpMax[i][1] = max(dpMax[i - 1][1] + nums[i][0], dpMax[i - 1][1] + nums[i][1], dpMax[i - 1][1] + nums[i][2])
#     dpMax[i][2] = max(dpMax[i - 1][2] + nums[i][1], dpMax[i - 1][2] + nums[i][2])
#     dpMin[i][0] = min(dpMin[i - 1][0] + nums[i][0], dpMin[i - 1][0] + nums[i][1])
#     dpMin[i][1] = min(dpMin[i - 1][1] + nums[i][0], dpMin[i - 1][1] + nums[i][1], dpMin[i - 1][1] + nums[i][2])
#     dpMin[i][2] = min(dpMin[i - 1][2] + nums[i][1], dpMin[i - 1][2] + nums[i][2])
#
# print(max(dpMax[n-1][0], dpMax[n-1][1], dpMax[n-1][2]), min(dpMin[n-1][0], dpMin[n-1][1], dpMin[n-1][2]))