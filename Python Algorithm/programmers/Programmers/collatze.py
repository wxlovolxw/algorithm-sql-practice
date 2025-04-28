n = 10


def solution(n):
    answer = []
    num = n
    answer.append(num)
    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            answer.append(num // 2)
            num = num // 2
        else:
            answer.append(3 * num + 1)
            num = 3 * num + 1

    return answer


print(solution(n))