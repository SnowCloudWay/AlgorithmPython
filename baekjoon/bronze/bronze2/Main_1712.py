# Bronze II _ 1712번 _ 순익분기점

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    if b >= c:
        print(-1)
    else:
        print(int(a/(c-b))+1)