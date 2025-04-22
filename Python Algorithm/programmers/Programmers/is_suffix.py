my_string = "banana"
is_suffix = "a"

def solution(my_string, is_suffix):
    a = list(my_string[len(my_string)-len(is_suffix):])
    b = list(is_suffix)

    return 1 if a == b else 0

print(solution(my_string, is_suffix)) 