# Silver III _ 2108 _ 통계학

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, sys.stdin.read().splitlines()))
nums.sort()

sys.stdout.write(str(round(sum(nums)/len(nums)))+'\n')
sys.stdout.write(str(nums[n//2])+'\n')
d = {}
for num in nums:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
s_d = sorted(d.items(), key=lambda item: (-item[1], item[0]))
if len(nums) > 1 and s_d[0][1] == s_d[1][1]:
    sys.stdout.write(str(s_d[1][0])+'\n')
else:
    sys.stdout.write(str(s_d[0][0])+'\n')
sys.stdout.write(str(max(nums) - min(nums))+'\n')



# import sys
# import statistics
# from collections import Counter
#
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, sys.stdin.read().splitlines()))
# nums.sort()
#
# sys.stdout.write(str(round(statistics.mean(nums)))+'\n')
#
# sys.stdout.write(str(statistics.median(nums))+'\n')
#
# mode_ = Counter(nums).most_common(2)
# if len(mode_) > 1 and mode_[0][1] == mode_[1][1]:
#     sys.stdout.write(str(mode_[1][0]) + '\n')
# else:
#     sys.stdout.write(str(mode_[0][0])+'\n')
#
# sys.stdout.write(str(max(nums) - min(nums))+'\n')