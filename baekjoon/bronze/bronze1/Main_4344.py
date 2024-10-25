# Bronze I _ 4344번 _ 평균은 넘겠지

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        scores = list(map(int, input().split()))
        cnt = 0

        for j in scores[1:]:
            avg = sum(scores[1:])/scores[0]
            if j > avg:
                cnt += 1

        per = (cnt/scores[0])*100
        print('{0:0.3f}%'.format(per))

# if __name__ == '__main__':
#     avg_score = []
#
#     n = int(input())
#
#     for i in range(n):
#         score = list(map(int, input().split()))
#         total_sum = 0
#         m = score[0]
#
#         for j in range(1, m + 1):
#             total_sum += score[j]
#
#         result = total_sum / m
#         avg_score.append(result)
#
#     for i in avg_score:
#         print(i)