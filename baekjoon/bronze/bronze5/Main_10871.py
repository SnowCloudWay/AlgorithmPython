# Bronze V _ 10871번 _ X보다 작은 수

if __name__ == '__main__':
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []

    for i in range(0, n):
        if nums[i] < x:
            result.append(nums[i])

    print(*result)