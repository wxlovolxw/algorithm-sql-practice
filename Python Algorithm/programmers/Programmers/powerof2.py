arr = [58, 172, 746, 89]

def solution(arr):
    answer = []
    i = 0
    while i < 11:
        if pow(2,i) <  len(arr) <= pow(2,i+1):
            arr.extend([0] * (pow(2,i+1) - len(arr)))
            break
        else : i += 1
    return arr

print(solution(arr))