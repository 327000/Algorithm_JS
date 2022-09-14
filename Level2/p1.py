#최댓값과 최솟값
def solution(s):
    answer = ''
    max_num = int(s.split()[0])
    min_num = int(s.split()[0])
    list_len = s.split()
    for i in range(1, len(list_len)):
        if int(s.split()[i]) > max_num:
            max_num = int(s.split()[i])
        elif int(s.split()[i]) < min_num:
            min_num = int(s.split()[i])

    answer = answer + str(min_num) + ' '
    answer = answer + str(max_num)

    return answer