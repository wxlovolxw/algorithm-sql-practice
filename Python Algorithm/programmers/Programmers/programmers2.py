
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]

ext = "date"
val_ext	= 20300501
sort_by = "remain"

def solution(data, ext, val_ext, sort_by):
    answer = []
    list = ['code','date','maximum','remain']
    idx = list.index(ext)

    for x in data :
        if x[idx] < val_ext :
            answer.append(x)

    answer.sort(key=lambda y: y[list.index(sort_by)])

    return answer

print(solution(data, ext, val_ext, sort_by))