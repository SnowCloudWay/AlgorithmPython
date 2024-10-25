# Bronze IV _ 5554번 _ 심부름 가는 길

if __name__ == '__main__':
    t = 0
    for _ in range(4):
        t += (int(input()))
    x = t // 60
    y = t % 60
    print(x)
    print(y)