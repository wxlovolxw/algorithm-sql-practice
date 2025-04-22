a = [1,2,3]

def solution(a) :
    answer = 0

    try :
        answer = a[4]

    except IndexError: pass

    return answer

print(solution(a))