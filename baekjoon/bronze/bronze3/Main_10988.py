# Bronze III _ 10988 _ 팰린드롬인지 확인하기

import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    if word == word[::-1]:
        print(1)
    else:
        print(0)