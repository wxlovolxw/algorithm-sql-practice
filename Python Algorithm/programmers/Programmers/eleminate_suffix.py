str_list = ["abc", "def", "ghi"]
ex = "ef"


def solution(str_list, ex):
    answer = ''.join([str for str in str_list if list(str)[len(str) - len(ex):] != list(ex)])

    return answer


print(solution(str_list, ex))