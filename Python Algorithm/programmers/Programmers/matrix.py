n = 3


def solution(n):
    answer = [[0] * n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1

    return answer


print(solution(n))