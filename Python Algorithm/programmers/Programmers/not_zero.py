n_str = "0010"

def solution(n_str):
    count = 0
    for num in list(n_str):
        if num == '0':
            count += 1
        else:
            break

    return ''.join(list(n_str)[count:])

print(solution(n_str))