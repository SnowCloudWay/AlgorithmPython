# Silver V _ 10814번 _ 나이순 정렬

import sys
from collections import OrderedDict
input = sys.stdin.readline

od = OrderedDict()
n = int(input())

for i in range(n):
    info = list(map(str, input().split()))
    od[i] = [int(info[0]), info[1]]

sorted_od = OrderedDict(sorted(od.items(), key=lambda x: x[1][0]))

for k, v in sorted_od.items():
    sys.stdout.write(str(v[0])+' '+v[1]+'\n')

# 너무 느림
# if __name__ == '__main__':
#     n = int(input())
#     members = [[0 for j in range(2)] for i in range(n)]
#     for i in range(0, n):
#         age, name = input().split()
#         members[i][0] = int(age)
#         members[i][1] = name
#     members.sort(key=lambda x: x[0])
#     for member in members:
#         print(member[0], member[1])