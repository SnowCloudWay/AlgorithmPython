# Bronze III _ 10872번 _ 팩토리얼

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)
