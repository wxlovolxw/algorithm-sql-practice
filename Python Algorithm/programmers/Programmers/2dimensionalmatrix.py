arr = [[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][j] == arr[j][i]:
                answer = 1
                break
            else: pass
    return answer

print(solution(arr))