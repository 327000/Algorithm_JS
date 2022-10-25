def solution(fish_list):
    shark_x = 0
    shark_y = 0
    shark_d = fish_list[0][1]
    global answer, max_num
    answer = 0
    fish_list[0][0] = 0
    dfs(fish_list, shark_x, shark_y, shark_d, answer)
    return answer
def dfs(fish_list, shark_x, shark_y, shark_d, max_num):
    max_num += fish_list[shark_x][shark_y]
    tmp = fish_list[shark_x][shark_y]
    fish_list[shark_x][shark_y] = 0
    global answer
    if max_num > answer:
        answer = max_num
    fish_move(fish_list, shark_x, shark_y)

    if shark_d == 1:
        i = 1
        while True:
            if shark_x - i >= 0:
                if fish_list[shark_x - i][shark_y] != 0:
                    shark_d = fish_list[shark_x - i][shark_y + 1]
                    dfs(fish_list, shark_x - i, shark_y, shark_d, max_num)
            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1

    if shark_d == 2:
        i = 1
        while True:
            if shark_x - i >= 0 and shark_y - (2 * i) >= 0:
                if fish_list[shark_x - i][shark_y - (2 * i)] != 0:
                    shark_d = fish_list[shark_x - i][shark_y - (2 * i) + 1]
                    dfs(fish_list, shark_x - i, shark_y - (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1

    if shark_d == 3:
        i = 1
        while True:
            if shark_y - (2 * i) >= 0:
                if fish_list[shark_x][shark_y - (2 * i)] != 0:
                    shark_d = fish_list[shark_x][shark_y - (2 * i) + 1]
                    dfs(fish_list, shark_x, shark_y - (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1
    if shark_d == 4:
        i = 1
        while True:
            if shark_x + i <= 3 and shark_y - (2 * i) >= 0:
                if fish_list[shark_x + i][shark_y - (2 * i)] != 0:
                    shark_d = fish_list[shark_x + i][shark_y - (2 * i) + 1]
                    dfs(fish_list, shark_x + i, shark_y - (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1
    if shark_d == 5:
        i = 1
        while True:
            if shark_x + i <= 3:
                if fish_list[shark_x + i][shark_y] != 0:
                    shark_d = fish_list[shark_x + i][shark_y + 1]
                    dfs(fish_list, shark_x + i, shark_y, shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1
    if shark_d == 6:
        i = 1
        while True:
            if shark_x + i <= 3 and shark_y + (2 * i) <= 7:
                if fish_list[shark_x + i][shark_y + (2 * i)] != 0:
                    shark_d = fish_list[shark_x + i][shark_y + (2 * i) + 1]
                    dfs(fish_list, shark_x + i, shark_y + (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1
    if shark_d == 7:
        i = 1
        while True:
            if shark_y + (2 * i) <= 7:
                if fish_list[shark_x][shark_y + (2 * i)] != 0:
                    shark_d = fish_list[shark_x][shark_y + (2 * i) + 1]
                    dfs(fish_list, shark_x, shark_y + (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1
    if shark_d == 8:
        i = 1
        while True:
            if shark_x - i >= 0 and shark_y + (2 * i) <= 7:
                if fish_list[shark_x - i][shark_y + (2 * i)] != 0:
                    shark_d = fish_list[shark_x - i][shark_y + (2 * i) + 1]
                    dfs(fish_list, shark_x - i, shark_y + (2 * i), shark_d, max_num)

            else:
                fish_list[shark_x][shark_y] = tmp
                max_num -= fish_list[shark_x][shark_y]
                return
            i += 1

def fish_move(fish_list, shark_x, shark_y):
    k = 1
    k_flag = False
    k_flag2 = False
    shark_p = fish_list[shark_x][shark_y]
    while True:
        for i in range(4):
            if k_flag == True:
                break
            for j in range(0, 8, 2):
                if shark_p == k:
                    k_flag = True
                    break
                if fish_list[i][j] == k:
                    cnt = 0
                    while True:
                        if fish_list[i][j + 1] == 1:
                            if i - 1 <= -1:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i - 1 == shark_x and j == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i - 1][j]
                                tmp2 = fish_list[i - 1][j + 1]
                                fish_list[i - 1][j] = fish_list[i][j]
                                fish_list[i - 1][j + 1] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 2:
                            if i - 1 <= -1 or j - 2 <= -1:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i - 1 == shark_x and j - 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i - 1][j - 2]
                                tmp2 = fish_list[i - 1][j - 1]
                                fish_list[i - 1][j - 2] = fish_list[i][j]
                                fish_list[i - 1][j - 1] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 3:
                            if j - 2 <= -1:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i == shark_x and j - 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i][j - 2]
                                tmp2 = fish_list[i][j - 1]
                                fish_list[i][j - 2] = fish_list[i][j]
                                fish_list[i][j - 1] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 4:
                            if i + 1 >= 4 or j - 2 <= -1:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i + 1 == shark_x and j - 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i + 1][j - 2]
                                tmp2 = fish_list[i + 1][j - 1]
                                fish_list[i + 1][j - 2] = fish_list[i][j]
                                fish_list[i + 1][j - 1] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 5:
                            if i + 1 >= 4:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i + 1 == shark_x and j == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i + 1][j]
                                tmp2 = fish_list[i + 1][j + 1]
                                fish_list[i + 1][j] = fish_list[i][j]
                                fish_list[i + 1][j + 1] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 6:
                            if i + 1 >= 4 or j + 2 >= 8:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i + 1 == shark_x and j + 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i + 1][j + 2]
                                tmp2 = fish_list[i + 1][j + 3]
                                fish_list[i + 1][j + 2] = fish_list[i][j]
                                fish_list[i + 1][j + 3] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 7:
                            if j + 2 >= 8:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            elif i == shark_x and j + 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i][j + 2]
                                tmp2 = fish_list[i][j + 3]
                                fish_list[i][j + 2] = fish_list[i][j]
                                fish_list[i][j + 3] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break

                        if fish_list[i][j + 1] == 8:
                            if i - 1 >= 4 or j + 2 >= 8:
                                fish_list[i][j + 1] = 1
                                cnt += 1
                            elif i - 1 == shark_x and j + 2 == shark_y:
                                fish_list[i][j + 1] += 1
                                cnt += 1
                            else:
                                tmp1 = fish_list[i - 1][j + 2]
                                tmp2 = fish_list[i - 1][j + 3]
                                fish_list[i - 1][j + 2] = fish_list[i][j]
                                fish_list[i - 1][j + 3] = fish_list[i][j + 1]
                                fish_list[i][j] = tmp1
                                fish_list[i][j + 1] = tmp2
                                k_flag = True
                                k_flag2 = True
                                break
                        if cnt == 8:
                            break
                if k_flag2 == True:
                    break
        if k == 16:
            break
        k_flag = False
        k_flag2 = False
        k += 1

print(solution([[7, 6, 2, 3, 15, 6, 9, 8],
[3, 1, 1, 8, 14, 7, 10, 1],
[6, 1, 13, 6, 4, 3, 11, 4],
[16, 1, 8, 7, 5, 2, 12, 2]]))