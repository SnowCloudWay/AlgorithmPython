# Bronze II _ 2750번 _ 수 정렬하기

if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(0, n):
        nums.append(int(input()))
    nums.sort()
    for num in nums:
        print(num)