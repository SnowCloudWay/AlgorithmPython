# Bronze V _ 3003번 _ 킹, 퀸, 룩, 비숍, 나이트, 폰

if __name__ == '__main__':
    k, q, r, b, n, p = map(int, input().split())
    print(1-k, 1-q, 2-r, 2-b, 2-n, 8-p)