N = int(input())
s_list = [list(map(int, input().split())) for _ in range(N * N)]

map_list = [[0 for _ in range(N)] for _ in range(N)]
w_list = [[0, 0] for _ in range(N * N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#맨처음학생은 무조건 가운데
map_list[(N - 1) // 2][(N - 1) // 2] = s_list[0][0]
w_list[0][0] = (N - 1) // 2
w_list[0][1] = (N - 1) // 2


cnt = 0
nx = 0
ny = 0
k = 1
while k != len(s_list):
    while True:
        for h in range(1, 5):
            if nx >= N or ny >= N or nx <= -1 or ny <= -1:
                
            if map_list[nx][ny] == s_list[k][h]:
                cnt += 1

