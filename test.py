import sys
import statistics
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

l = ((1, 2), (2, 3), (3, 4))
for i in l:
    for a in i:
        print(a)