# Bronze IV _ 10808번 _ 알파벳 개수

if __name__ == '__main__':
    alphabets = [0 for _ in range(26)]
    n = input()

    for i in n:
        alphabets[ord(i) - ord('a')] += 1

    for i in alphabets:
        print(i, end=' ')