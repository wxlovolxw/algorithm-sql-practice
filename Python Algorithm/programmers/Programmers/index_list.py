my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]

def solution(my_string, index_list):
    answer = []
    len(index_list)
    for index, num in enumerate(index_list):
        answer.append(list(my_string)[index_list[index]])
    return ''.join(answer)


print(solution(my_string,index_list))