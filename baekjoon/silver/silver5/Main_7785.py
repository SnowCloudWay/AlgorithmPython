# Silver V _ 7785번 _ 회사에 있는 사람

import sys

if __name__ == '__main__':
    # 셋
    n = int(input())

    st = set()
    for _ in range(n):
        name, state = map(str, sys.stdin.readline().split())
        if state == "enter":
            st.add(name)
        elif state == "leave":
            st.discard(name)

    print('\n'.join(sorted(st, reverse=True)))

    # 딕셔너리
    # n = int(input())
    #
    # d = {}
    # for _ in range(n):
    #     name, state = map(str, sys.stdin.readline().split())
    #     if state == "enter":
    #         d[name] = state
    #     elif state == "leave":
    #         del d[name]
    #
    # print('\n'.join(sorted(d.keys(), reverse=True)))

    # 리스트(스택) = 시간초과
    # n = int(input())
    #
    # l = []
    # for _ in range(n):
    #     name, state = map(str, sys.stdin.readline().split())
    #     if state == "enter":
    #       l.append(name)
    #     elif state == "leave":
    #         l.remove(name)
    #
    # print('\n'.join(sorted(l, reverse=True)))