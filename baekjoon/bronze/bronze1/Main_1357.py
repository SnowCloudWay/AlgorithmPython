# Bronze I _ 1357 _ 뒤집힌 덧셈

import sys
input = sys.stdin.readline

a, b = input().split()
c = int(a[::-1]) + int(b[::-1])

sys.stdout.write(str(int(str(c)[::-1])))