# Bronze IV _ 10156번 _ 과자

if __name__ == '__main__':
    k, n, m = map(int, input().split())

    money = k * n - m

    if money < 0:
        money = 0

    print(money)