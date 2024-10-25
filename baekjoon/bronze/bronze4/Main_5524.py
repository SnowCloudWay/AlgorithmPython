# Bronze IV _ 5524번 _ 입실 관리

if __name__ == '__main__':
    n = int(input())
    checkInList = []
    for i in range(0, n):
        checkInList.append(input().lower())
    for people in checkInList:
        print(people)