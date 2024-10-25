# Bronze IV _ 5543번 _ 상근날드

if __name__ == '__main__':
    burgurA = int(input())
    burgurB = int(input())
    burgerC = int(input())
    drinkA = int(input())
    drinkB = int(input())

    minSet = min(burgurA, min(burgurB, burgerC)) + min(drinkA, drinkB) - 50
    print(minSet)