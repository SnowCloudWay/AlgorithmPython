# Bronze I _ 2869번 _ 달팽이는 올라가고 싶다

if __name__ == '__main__':
    a, b, v = map(int, input().split())
    day = (v - a) / (a - b) + 1
    print(int(day) if day == int(day) else int(day)+1)
