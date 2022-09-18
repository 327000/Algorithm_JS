#영어 끝말잇기
import math
def solution(n, words):
    answer = []
    cnt1 = 0
    cnt2 = 0
    esc_break = True

    for i in range(len(words)):
        if not esc_break:
            break
        elif i != 0:
            if words[i][0] != words[i - 1][-1]:
                cnt1 = (i + 1) % n
                cnt2 = math.ceil((i + 1) / n)
                if cnt1 == 0:
                    cnt1 = n
                break
        for j in range(i):
            if words[i] == words[j]:
                cnt1 = (i + 1) % n
                cnt2 = math.ceil((i + 1) / n)
                if cnt1 == 0:
                    cnt1 = n
                esc_break = False
                break
    answer.append(cnt1)
    answer.append(cnt2)
    return answer