
num = 12
def count(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = (num - 1) / 2
            count += 1

    return count

print(count(num))