# Silver V _ 25757 _ 임스와 함께하는 미니게임

import sys
input = sys.stdin.readline

n, game = input().split()
s = set(sys.stdin.read().splitlines())
cnt = 0

# if game == 'Y':
#     cnt = len(s)
# elif game == 'F':
#     cnt = len(s) // 2
# else:
#     cnt = len(s) // 3

match game:
    case 'Y':
        cnt = len(s)
    case 'F':
        cnt = len(s) // 2
    case _:
        cnt = len(s) // 3

sys.stdout.write(str(cnt))