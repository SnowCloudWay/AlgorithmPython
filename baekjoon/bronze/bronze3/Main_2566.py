# Bronze III _ 2566번 _ 최댓값

if __name__ == '__main__':
    table = [list(map(int, input().split())) for _ in range(9)]

    max_num = 0
    max_row, max_col = 0, 0
    for row in range(9):
        for col in range(9):
            if max_num <= table[row][col]:
                max_row = row + 1
                max_col = col + 1
                max_num = table[row][col]

    print(max_num)
    print(max_row, max_col)