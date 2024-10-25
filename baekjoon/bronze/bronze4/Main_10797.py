# Bronze IV _ 10797번 _ 10부제

if __name__ == '__main__':
    day = int(input())
    carNum = list(map(int, input().split()))
    cnt = 0

    for i in carNum:
        if i == day:
            cnt += 1

    print(cnt)
