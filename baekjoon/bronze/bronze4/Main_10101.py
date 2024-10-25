# Bronze IV _ 10101번 _ 삼각형 외우기

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    elif (a + b + c == 180) and (a == b or a == c or b == c):
        print("Isosceles")
    elif (a + b + c == 180) and (a != b and a != c and b != c):
        print("Scalene")
    else:
        print("Error")