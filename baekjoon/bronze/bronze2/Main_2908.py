# Bronze II _ 2908번 _ 상수

if __name__ == '__main__':
    A, B = map(int, input().split())
    re_A = int(str(A)[::-1])
    re_B = int(str(B)[::-1])
    print(max(re_A, re_B))