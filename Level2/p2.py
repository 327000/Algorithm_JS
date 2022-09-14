#이진 변환 반복하기
def solution(s):
    answer = []
    cnt = 0
    cnt_zero = 0
    def recurs(s, cnt):
        i = 0
        while i < len(s):
            if s[i] == '0':
                s = s[:i] + s[i + 1:]
                i -= 1
                cnt += 1
            i += 1
        a = bin(len(s))
        a = a[2:]
        return a, cnt
    while True:
        if s != '1':
            s, cnt_zero = recurs(s, cnt_zero)
            cnt += 1
        else:
            break
    answer.append(cnt)
    answer.append(cnt_zero)
    return answer
