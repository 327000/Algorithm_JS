#k진수에서 소수 개수 구하기
import math
def solution(n, k):
    answer = 0

    prime_list = []
    d = n
    prime_str = ""
    while True:
        prime_list.append(d % k)
        d //= k
        if d == 0:
            break
        elif d // k == 0:
            prime_list.append(d)
            break

    for i in range(len(prime_list) - 1, -1, -1):
        if prime_list[i] != 0:
            prime_str += str(prime_list[i])
            if i == 0:
                if isPrime(int(prime_str)):
                    answer += 1
                    prime_str = ""
        elif prime_list[i] == 0:
            if prime_list[i + 1] == 0:
                continue
            elif isPrime(int(prime_str)):
                answer += 1
                prime_str = ""
            elif not isPrime(int(prime_str)):
                prime_str = ""

    return answer


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


print(solution(1, 3))
