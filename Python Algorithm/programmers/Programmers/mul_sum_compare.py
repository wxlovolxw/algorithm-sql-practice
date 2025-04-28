num_list = [3, 4, 5, 2, 1]


def solution(num_list):
    answer = 1
    sum_num = 0
    mul_num = 1
    for i in num_list:
        sum_num += i * i
        mul_num *= i

    if sum_num < mul_num: answer = 0

    return answer


print(solution(num_list))