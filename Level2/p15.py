#게임 맵 최단거리
from collections import deque
def solution(maps):
    w = len(maps)
    l = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > w - 1 or ny < 0 or ny > l - 1:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[w - 1][l - 1]

    bfs(0, 0)
    if maps[w - 1][l - 1] == 1:
        return -1
    return maps[w - 1][l - 1]
