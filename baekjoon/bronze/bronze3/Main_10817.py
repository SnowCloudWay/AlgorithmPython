# Bronze III _ 10817번 _ 세 수

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[1])