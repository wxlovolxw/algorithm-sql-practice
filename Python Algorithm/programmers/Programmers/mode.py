code = "abc1abc1abc"

def solution(code):
    mode = 0
    answer = ''
    for i, x in enumerate(code):
        if x == '1' and mode == 0:
            mode = 1
        elif x == '1' and mode == 1:
            mode = 0
        elif (x != 1) and (mode == 0) and (i % 2 == 0):
            answer += x
        elif (x != 1) and (mode == 1) and (i % 2 != 0):
            answer += x

    return answer

print(solution(code))