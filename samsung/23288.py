# import sys
from collections import deque
# input = sys.stdin.readline
# n, m, x, y, k = map(int, input().split())

def solution(map_list, N, M, K):
    d_x = 0
    d_y = 1
    answer = 0
    dice_d = 1
    dice_list = [2, 4, 5, 3, 6, 1]
    for i in range(K):
        c_map_list = [[False for i in range(M)] for j in range(N)]
        answer += (bfs(map_list, c_map_list, dice_list, d_x, d_y, N, M))
        if map_list[d_x][d_y] < dice_list[3]:
            dice_d += 1
            if dice_d == 5:
                dice_d = 1
        elif map_list[d_x][d_y] > dice_list[3]:
            dice_d -= 1
            if dice_d == 0:
                dice_d = 4

        if dice_d == 1:
            d_y += 1
            if d_y == M:
                d_y -= 2
                dice_d = 3
        elif dice_d == 2:
            d_x += 1
            if d_x == N:
                d_x -= 2
                dice_d = 4
        elif dice_d == 3:
            d_y -= 1
            if d_y == -1:
                d_y += 2
                dice_d = 1
        elif dice_d == 4:
            d_x -= 1
            if d_x == -1:
                d_x += 2
                dice_d = 2
        dice_list = move(dice_list, dice_d)
    return answer


def bfs(map_list, c_map_list, dice_list, d_x, d_y, N, M):
    queue = deque()
    queue.append((d_x, d_y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    c_map_list[d_x][d_y] = True
    while queue:
        d_x, d_y = queue.popleft()
        for i in range(4):
            nx = d_x + dx[i]
            ny = d_y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if map_list[nx][ny] != map_list[d_x][d_y] and c_map_list[nx][ny] == True:
                continue
            if map_list[nx][ny] == map_list[d_x][d_y] and c_map_list[nx][ny] == False:
                c_map_list[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))
    return map_list[d_x][d_y] * cnt


def move(dice_list, dice_d):  # dice_list 세로줄 0123 왼쪽 오른쪽 아랫면은 3idx
    dice_list2 = dice_list.copy()
    if dice_d == 1:  # 동
        dice_list[0] = dice_list2[0]
        dice_list[1] = dice_list2[4]
        dice_list[2] = dice_list2[2]
        dice_list[3] = dice_list2[5]
        dice_list[4] = dice_list2[3]
        dice_list[5] = dice_list2[1]

    elif dice_d == 2:  # 남
        dice_list[0] = dice_list2[3]
        dice_list[1] = dice_list2[0]
        dice_list[2] = dice_list2[1]
        dice_list[3] = dice_list2[2]
        dice_list[4] = dice_list2[4]
        dice_list[5] = dice_list2[5]

    elif dice_d == 3:  # 서
        dice_list[0] = dice_list2[0]
        dice_list[1] = dice_list2[5]
        dice_list[2] = dice_list2[2]
        dice_list[3] = dice_list2[4]
        dice_list[4] = dice_list2[1]
        dice_list[5] = dice_list2[3]

    elif dice_d == 4:  # 북
        dice_list[0] = dice_list2[1]
        dice_list[1] = dice_list2[2]
        dice_list[2] = dice_list2[3]
        dice_list[3] = dice_list2[0]
        dice_list[4] = dice_list2[4]
        dice_list[5] = dice_list2[5]

    return dice_list


print(solution([[4, 1, 2, 3, 3], [6, 1, 1, 3, 3], [5, 6, 1, 3, 2], [5, 5, 6, 5, 5]], 4, 5, 1000))
