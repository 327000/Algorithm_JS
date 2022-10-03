# 네트워크
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    global new_connection
    new_connection = False
    for i in range(n):
        dfs(n, computers, i, visited)
        if new_connection == True:
            answer += 1
            new_connection = False
    return answer


def dfs(n, computers, i, visited):
    global new_connection
    for j in range(n):
        if computers[i][j] == 1:
            if visited[j] == False:
                visited[j] = True
                new_connection = True
                if i != j:
                    dfs(n, computers, j, visited)
    return
