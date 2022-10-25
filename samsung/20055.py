def solutuion(con_list, N, K):
    on_robot = [False for i in range(N)]
    f_robot = -1
    answer = 0
    while True:
        cnt = 0
        for i in range(2 * N):
            if con_list[i] == 0:
                cnt += 1
        if cnt >= K:
            break

        f_robot = conMove(con_list, on_robot, f_robot, N)
        f_robot = robotMove(con_list, on_robot, N, f_robot)
        f_robot = onRobot(con_list, on_robot, f_robot, N)
        answer += 1
    return answer


def conMove(con_list, on_robot, f_robot, N):
    con_list2 = con_list.copy()
    on_robot2 = on_robot.copy()
    flag = False
    for i in range(2 * N - 1):
        con_list[i + 1] = con_list2[i]

    con_list[0] = con_list2[-1]
    on_robot[0] = False

    for i in range(N - 1):
        on_robot[i + 1] = on_robot2[i]

    if f_robot != -1:
        f_robot += 1
    if on_robot[-1]:
        for j in range(N - 2, -1, -1):
            if on_robot[j]:
                f_robot = j
                flag = True
                break
        if flag == False:
            f_robot = -1
        on_robot[-1] = False
    return f_robot


def robotMove(con_list, on_robot, N, f_robot):
    flag = False
    if f_robot == -1:
        i = 1
    else:
        i = f_robot + 1

    while True:
        if con_list[i] != 0 and on_robot[i] == False and on_robot[i - 1] == True:
            con_list[i] -= 1
            if i != N - 1:
                on_robot[i - 1] = False
                on_robot[i] = True
                if i - 1 == f_robot:
                    f_robot += 1
            else:
                on_robot[i - 1] = False
                for j in range(N - 1, -1, -1):
                    if on_robot[j]:
                        f_robot = j
                        flag = True
                        break
                if flag == False:
                    f_robot = -1
        i -= 1

        if i == 0:
            break
    return f_robot


def onRobot(con_list, on_robot, f_robot, N):
    e_robot_flag = False
    for i in range(N):
        if on_robot[i] == True:
            e_robot_flag = True

    if con_list[0] != 0 and on_robot[0] == False:
        on_robot[0] = True
        con_list[0] -= 1
        if e_robot_flag == False:
            f_robot += 1
    return f_robot

N, K = map(int, input().split())
con_list = list(map(int, input().split()))  # 컨베이어 벨트 - 1차원 리스트로 표현(2*N개)

print(solutuion(con_list, N, K))

#print(solutuion([10, 1, 10, 6, 3, 4, 8, 2], 4, 5))
#print(solutuion([1, 2, 1, 2, 1, 2], 3, 2))
#print(solutuion([10, 10, 10, 10, 10, 10], 3, 6))
#print(solutuion([100, 99, 60, 80, 30, 20, 10, 89, 99, 100], 5, 8))