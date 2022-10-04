def solution(tickets):
    answer = []
    global last_coun
    last_coun = 'ICN'
    tickets.sort()
    visited = [False for i in range(len(tickets))]
    answer.append(last_coun)
    dfs(tickets, last_coun, visited, answer)

    return answer

def dfs(tickets, last_coun, visited, answer):
    for i in range(len(tickets)):
        if tickets[i][0] == last_coun and visited[i] == False:
            visited[i] = True
            answer.append(tickets[i][1])
            last_coun = tickets[i][1]
            dfs(tickets, last_coun, visited, answer)
            visited[i] = False
            last_coun = answer[-1]
    if len(answer) != len(tickets) + 1:
        answer.pop()
        return

# def bfs(tickets, queue, last_coun, answer):
#     while True:
#         for j in range(len(tickets)):
#             if tickets[j][0] == last_coun:
#                 queue.put(tickets[j][1])
#         n = queue.get()
#         tickets.remove([last_coun, n])
#         answer.append(n)
#
#         while not queue.empty():
#             queue.get()
#         last_coun = n
#         if len(tickets) == 0:
#             return
