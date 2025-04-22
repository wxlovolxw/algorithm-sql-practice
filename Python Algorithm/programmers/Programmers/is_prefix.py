my_string = "banana"
is_prefix = "ban"
def solution(my_string, is_prefix):
    answer = 0
    lenght = len(list(is_prefix))
    if list(my_string)[:lenght] == list(is_prefix):
        answer = 1
    return answer

print(solution(my_string,is_prefix))