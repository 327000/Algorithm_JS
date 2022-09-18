#점프와 순간 이동
def solution(n):
    bat_cnt = 1
    while True:
        if n == 1:
            break
        elif n % 2 != 0:
            bat_cnt += 1
            n -= 1
        elif n == 2:
            break
        else:
            n = n / 2
    return bat_cnt
