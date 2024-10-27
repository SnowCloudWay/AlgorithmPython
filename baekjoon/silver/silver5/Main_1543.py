# Silver V _ 1543 _ 문서 검색

import sys
input = sys.stdin.readline

s = input().strip()
word = input().strip()
cnt = 0
idx = 0

while idx <= len(s) - len(word):
    if s[idx:idx+len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx += 1

sys.stdout.write(str(cnt))