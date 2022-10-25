def solution(one_list, N, f_d, s, answer):
    one_list = fire(f_d, one_list, s)
    answer, one_list = explosion(one_list, answer)
    one_list = charge_Marble(one_list)
    return answer, one_list


def change_list(map_list, N):
    t_list = [[False for i in range(N)] for i in range(N)]
    one_list = []
    turn_flag = False
    w_flag = False
    h_flag = True
    i = 0
    j = N - 1
    for k in range(N - 1):
        one_list.append(map_list[0][k])
        t_list[0][k] = True
    while True:
        if i >= N or j >= N or i <= -1 or j <= -1:
            break
        if i == (N - 1) / 2 and j == (N - 1) / 2:
            break
        one_list.append(map_list[i][j])
        t_list[i][j] = True
        if w_flag and turn_flag == False:
            j += 1
            if j == N - 1:
                w_flag = False
                h_flag = True
                turn_flag = False
            if t_list[i][j]:
                w_flag = False
                h_flag = True
                turn_flag = False
                j -= 1
                i += 1
        elif h_flag and turn_flag == False:
            i += 1
            if i == N - 1:
                w_flag = True
                h_flag = False
                turn_flag = True
            if t_list[i][j]:
                w_flag = True
                h_flag = False
                turn_flag = True
                i -= 1
                j -= 1
        elif w_flag and turn_flag == True:
            j -= 1
            if j == 0:
                w_flag = False
                h_flag = True
                turn_flag = True
            if t_list[i][j]:
                w_flag = False
                h_flag = True
                turn_flag = True
                j += 1
                i -= 1
        elif h_flag and turn_flag == True:
            i -= 1
            if i == 0:
                w_flag = True
                h_flag = False
                turn_flag = False
            if t_list[i][j]:
                w_flag = True
                h_flag = False
                turn_flag = False
                i += 1
                j += 1
    one_list.reverse()
    return one_list

def fire(f_d, one_list, s):
    if f_d == 1:
        n = 7
        cnt = 7
        c_cnt = 0
        for _ in range(s):
            one_list[n - 1] = 0
            cnt += 8
            n = n + cnt
        for j in range(len(one_list)):
            if one_list[j] == 0:
                if j != len(one_list):
                    one_list = one_list[:j] + one_list[j + 1:]
                c_cnt += 1
                one_list.append(0)
            if c_cnt == s:
                break

    elif f_d == 2:
        n = 3
        cnt = 3
        c_cnt = 0
        for _ in range(s):
            one_list[n - 1] = 0
            cnt += 8
            n = n + cnt
        for j in range(len(one_list)):
            if one_list[j] == 0:
                if j != len(one_list):
                   one_list = one_list[:j] + one_list[j + 1:]
                c_cnt += 1
                one_list.append(0)
            if c_cnt == s:
                break

    elif f_d == 3:
        n = 1
        cnt = 1
        c_cnt = 0
        for _ in range(s):
            one_list[n - 1] = 0
            cnt += 8
            n = n + cnt
        for j in range(len(one_list)):
            if one_list[j] == 0:
                if j != len(one_list):
                    one_list = one_list[:j] + one_list[j + 1:]
                c_cnt += 1
                one_list.append(0)
            if c_cnt == s:
                break

    elif f_d == 4:
        n = 5
        cnt = 5
        c_cnt = 0
        for _ in range(s):
            one_list[n - 1] = 0
            cnt += 8
            n = n + cnt
        for j in range(len(one_list)):
            if one_list[j] == 0:
                if j != len(one_list):
                    one_list = one_list[:j] + one_list[j + 1:]
                c_cnt += 1
                one_list.append(0)
            if c_cnt == s:
                break
    return one_list


def explosion(one_list, answer):
    while True:
        i = 1
        flag = False
        cnt = 0
        end_flag = False
        while i != len(one_list):
            if i >= len(one_list) or i <= -1:
                break
            if one_list[i] == one_list[i - 1]:
                if flag == False:
                    s = i - 1
                flag = True
                cnt += 1
            else:
                flag = False
                if cnt >= 3:
                    end_flag = True
                    answer += one_list[i - 1] * (i - s)
                    if s != len(one_list):
                        one_list = one_list[:s] + one_list[i:]
                    for _ in range(i - s + 1):
                        one_list.append(0)
                    i = 0
                    s = 0
                cnt = 0
            i += 1
        if end_flag == False:
            break
    return answer, one_list


def charge_Marble(one_list):
    flag = False
    i = 0
    cnt = 0
    while True:
        if i >= len(one_list) - 1 or i <= -1:
            break
        if one_list[i] == one_list[i + 1]:
            flag = True
            cnt += 1
        elif one_list[i] != one_list[i + 1]:
            if cnt == 1 or cnt == 0:
                if flag == True:
                    one_list[i - 1] = 2
                    flag = False
                else:
                    one_list.insert(i, 1)
                    i += 1
                cnt = 0
            else:
                if flag == True:
                    one_list[i - 2] = 3
                    if i != len(one_list):
                        del one_list[i]
                    flag = False
                    cnt = 0
                    one_list.append(0)
                    i -= 1
        i += 1
        if one_list[i] == 0:
            break
    return one_list


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]
global answer
answer = 0

one_list = change_list(board, N)

for i in range(M):
    answer, one_list = solution(one_list, N, magics[i][0], magics[i][1], answer)

print(answer)

# 3 1
# 0 2 2
# 2 0 1
# 2 2 2
# 4 1
#

