# Bronze III _ 5597번 _ 과제 안 내신 분..?
# 다시 풀기

if __name__ == '__main__':
    students = [i for i in range(1, 31)]

    for _ in range(28):
        applied = int(input())
        students.remove(applied)

    print(min(students))
    print(max(students))