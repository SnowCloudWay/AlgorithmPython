# Bronze IV _ 1264번 _ 모음의 개수

if __name__ == '__main__':
    while True:
        tc = input()
        tcList = list(tc)
        cnt = 0
        if tc == '#':
            break
        for i in tcList:
            if i in 'aeiou' or i in 'AEIOU':
                cnt += 1
        print(cnt)