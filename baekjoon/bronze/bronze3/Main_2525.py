# Bronze III _ 2525번 _ 오븐 시계

if __name__ == '__main__':

    hour, minute = map(int, input().split())
    cookTime = int(input())

    if minute + cookTime < 60:
        minute += cookTime

    elif minute + cookTime >= 60:
        time = (cookTime + minute) / 60
        hour += int(time)
        minute += cookTime - (60 * int(time))

    if hour >= 24:
        hour -= 24

    print(hour, minute)