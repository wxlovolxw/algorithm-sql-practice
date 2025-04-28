arr = [3, 2, 4, 1, 3]
flag = [True, False, True, False, False]


def solution(arr, flag):
    answer = []
    for i, x in enumerate(flag):
        if x == True:
            answer.extend([arr[i]] * (arr[i] * 2))
        else:
            answer = answer[:-arr[i]]

    return answer


print(solution(arr, flag))