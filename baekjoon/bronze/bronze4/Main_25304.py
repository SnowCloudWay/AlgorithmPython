# Bronze IV _ 25304번 _ 영수증

if __name__ == '__main__':
    X = int(input())
    N = int(input())
    total = 0

    for _ in range(N):
        a, b = map(int, input().split())
        total += a * b

    if X == total:
        print("Yes")
    else:
        print("No")