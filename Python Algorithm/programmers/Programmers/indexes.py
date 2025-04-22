myString = "banana"
pat = "ana"

def solution(myString, pat):
    count = 0
    for i, x in enumerate(myString[:-len(pat)+1]):
        if myString[i:i+len(pat)] == pat:
            count += 1
    return count

print(solution(myString, pat))