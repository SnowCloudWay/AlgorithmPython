# Bronze V _ 10952번 _ A+B - 5

if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break
        else:
            print(a + b)