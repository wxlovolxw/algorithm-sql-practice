arr = [1, 2, 3, 100, 99, 98]


def solution(arr):
    answer = []
    for x in arr:
        count = 0
        while ((x < 50) and (x % 2 != 0)) or ((x >= 50) and (x % 2 == 0)):
            if ((x < 50) and (x % 2 != 0)):
                x = x * 2 + 1
                count += 1
            elif ((x >= 50) and (x % 2 == 0)):
                x = x / 2
                count += 1

        answer.append(count)

    return max(answer)


print(solution(arr))