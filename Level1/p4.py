# LEVEL_1 : 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for i in range(len(win_nums)):
        if lottos[i] == 0:
            zero_cnt += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1

    if cnt + zero_cnt == 6:
        answer.append(1)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    elif cnt + zero_cnt == 5:
        answer.append(2)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    elif cnt + zero_cnt == 4:
        answer.append(3)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    elif cnt + zero_cnt == 3:
        answer.append(4)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    elif cnt + zero_cnt == 2:
        answer.append(5)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    else:
        answer.append(6)
        if cnt == 0:
            answer.append(6 - cnt)
        else:
            answer.append(7 - cnt)
    return answer