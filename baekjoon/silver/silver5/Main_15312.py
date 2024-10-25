# Silver V _ 15312 _ 이름 궁합

import sys
input = sys.stdin.readline

alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input().strip()
b = input().strip()

l = []
for i in range(len(a)):
    l.append(alphabet[ord(a[i])-65])
    l.append(alphabet[ord(b[i])-65])

while len(l) != 2:
    l = [(l[i] + l[i+1]) % 10 for i in range(len(l)-1)]

sys.stdout.write(str(l[0]) + str(l[1]))




# 딕셔너리 사용
# alphabet = {'A': 3, 'B': 2, 'C' : 1, 'D' : 2, 'E' : 3, 'F' : 3, 'G' : 2, 'H' : 3, 'I' : 3, 'J' : 2, 'K' : 2, 'L' : 1, 'M' : 2, 'N' : 2, 'O': 1, 'P' : 2, 'Q': 2, 'R': 2, 'S' : 1, 'T' : 2, 'U': 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1}
# l = []
#
# a = input().strip()
# b = input().strip()
#
# for i in range(len(a)):
#     l.append(alphabet[a[i]])
#     l.append(alphabet[b[i]])
#
# while True:
#     ll = []
#     for i in range(len(l)-1):
#         ll.append((l[i] + l[i+1]) % 10)
#     l = ll
#     if len(l) == 2:
#         print(''.join(list(map(str, ll))))
#         break