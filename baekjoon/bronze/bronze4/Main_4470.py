# Bronze IV _ 4470번 _ 줄번호

if __name__ == '__main__':
    n = int(input())
    strList = []

    for i in range(n):
        strList.append(str(i+1) + ". " + input())

    for j in strList:
        print(j)