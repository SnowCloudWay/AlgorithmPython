# Silver III _ 15815번 _ 천재 수학자 성필

if __name__ == '__main__':
    l = input()
    s = []

    for i in l:
        if i not in "+-*/":
            s.append(int(i))
        else:
            a = s.pop()
            b = s.pop()
            if i == '+': s.append(b + a)
            elif i == '-': s.append(b - a)
            elif i == '*': s.append(b * a)
            elif i == '/': s.append(b // a)

    print(s.pop())
