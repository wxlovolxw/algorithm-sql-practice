arr = [0, 1, 2, 3, 4, 5]
query = [4, 1, 2]


def solution(arr, query):
    for i, x in enumerate(query):
        if i % 2 == 0:
            arr = arr[:x]
        else:
            arr = arr[x:]

    answer = []
    return answer


print(solution(arr, query))