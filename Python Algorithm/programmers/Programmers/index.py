arr = [0, 0, 0, 1]
idx = 1

def solution(arr, idx):
    answer = -1
    for i, x in enumerate(arr):
        if i > idx and x != 0:
            answer = i
            break
        else : pass
    return answer

print(solution(arr, idx))