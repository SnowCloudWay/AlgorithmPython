# Silver IV _ 1269 _ 대칭 차집합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

sys.stdout.write(str(len(a - b) + len(b - a)))