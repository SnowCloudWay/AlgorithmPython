# Bronze IV _ 10768번 _ 특별한 날

if __name__ == '__main__':
    month = int(input())
    day = int(input())

    if month == 2:
        if day == 18:
            print("Special")
        elif day < 18:
            print("Before")
        elif day > 18:
            print("After")
    elif month < 2:
        print("Before")
    elif month > 2:
        print("After")