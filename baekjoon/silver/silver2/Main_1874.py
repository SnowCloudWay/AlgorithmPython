# Silver II _ 1874번 _ 스택 수열

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    s = []
    result = []
    cnt = 1

    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
        while num >= cnt:
            s.append(cnt)
            result.append("+")
            cnt += 1
        if num == s[-1]:
            s.pop()
            result.append("-")
        else:
            print("NO")
            exit()

    print('\n'.join(result))