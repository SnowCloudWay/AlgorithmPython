# Silver IV _ 9012번 _ 괄호

# 스택
# if __name__ == '__main__':
#     T = int(input())
#
#     for _ in range(T):
#         tc = input()
#         stack = []
#
#         for i in tc:
#             if i == '(':
#                 stack.append(i)
#             elif i == ')':
#                 if '(' in stack:
#                     stack.pop()
#                 else:
#                     stack.append(i)
#                     break
#         if stack:
#             print("NO")
#         else:
#             print("YES")

# 스택 X
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
