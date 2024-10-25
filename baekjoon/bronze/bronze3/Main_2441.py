# Bronze III _ 2441번 _ 별 찍기 - 4

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(" "*(i-1) + "*"*(n-i+1))