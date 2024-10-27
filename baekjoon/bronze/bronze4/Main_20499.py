# Bronze IV _ 20499 _ Darius님 한타 안 함?

import sys
input = sys.stdin.readline

k, d, a = map(int, input().split('/'))

if k + a < d or d == 0:
    sys.stdout.write('hasu')
else:
    sys.stdout.write('gosu')