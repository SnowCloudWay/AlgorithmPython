# Bronze IV _ 9295번 _ 주사위

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        print("Case {0}: {1}".format(i+1, a+b))