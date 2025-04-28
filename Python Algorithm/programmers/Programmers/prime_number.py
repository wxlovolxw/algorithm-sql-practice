counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n: # n의 제곱근보다는 큰값으로 나눠야함. 곱셈과 나눗셈 두번의 연산이므로 2개씩 카운트
        counter += 2
        if n % prime[i] == 0:
            break # 나눠떨어진다면 소수가 아님
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter +=1