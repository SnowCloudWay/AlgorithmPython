# Silver V _ 2941 _ 크로아티아 알파벳

import sys

li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = sys.stdin.readline().rstrip()

for i in li:
    if i in alphabet:
        alphabet = alphabet.replace(i, '!')

sys.stdout.write(str(len(alphabet)))