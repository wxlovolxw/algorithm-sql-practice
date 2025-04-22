board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]]
h = 3
w = 0


def solution(board, h, w):
    answer = 0

    list = []

    if h == 0 and w == 0:
        pass
    elif h == 0 and w != 0:
        list.append(board[h][w - 1])
    elif w == 0 and h != 0:
        list.append(board[h - 1][w])
    else:
        list.append(board[h - 1][w])
        list.append(board[h][w - 1])

    try :
        list.append(board[h + 1][w])
    except IndexError:
        pass

    try :
        list.append(board[h][w + 1])
    except IndexError:
        pass

    answer = list.count(board[h][w])

    return answer

print(solution(board, h, w))