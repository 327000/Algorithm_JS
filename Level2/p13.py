#N진수 게임
def change(n, i):
    answer = ''
    tmp = ['A', "B", 'C', 'D','E','F']
    while n:
        num = n%i
        if num < 10:
            answer = str(num) + answer
        else:
            answer = tmp[num-10] + answer
        n = n//i
    return answer

def solution(n, t, m, p):
    length = 0
    i = 1
    answer = '0'
    answers = ''
    while length < t*m:
        tmp = change(i, n)
        answer += tmp
        length += len(tmp)
        i += 1
    for x in range(p-1, len(answer),m):
        answers += answer[x]
    return answers[:t]