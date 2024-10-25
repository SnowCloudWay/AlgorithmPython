# Bronze II _ 10809번 _ 알파벳 찾기

if __name__ == '__main__':
    S = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        print(S.find(i), end=' ')