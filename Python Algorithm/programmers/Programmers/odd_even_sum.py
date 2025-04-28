num_list = [3, 4, 5, 2, 1]

def solution(num_list):
    odd_list = []
    even_list = []
    for i in num_list:
        if i % 2 : odd_list.append(i)
        else : even_list.append(i)

    answer = int(''.join(list(map(str,odd_list)))) + int(''.join(list(map(str,even_list))))

    return answer

print(solution(num_list))