# Silver IV _ 1302 _ 베스트셀러

import sys
from collections import defaultdict
input = sys.stdin.readline

dd = defaultdict(int)
n = int(input())

for _ in range(n):
    dd[input().strip()] += 1

s_dd = sorted(dd.items(), key=lambda item: (-item[1], item[0]))
sys.stdout.write(str(s_dd[0][0]))