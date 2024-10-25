# Bronze V _ 14681번 _ 사분면 고르기

if __name__ == '__main__':
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)