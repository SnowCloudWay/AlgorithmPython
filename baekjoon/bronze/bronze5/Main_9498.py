# Bronze V _ 9498번 _ 시험 성적

if __name__ == '__main__':
    score = int(input())

    if score < 60:
        print("F")
    elif score <= 69:
        print("D")
    elif score <= 79:
        print("C")
    elif score <= 89:
        print("B")
    else:
        print("A")