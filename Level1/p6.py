# Level_1 : 신규 아이디 추천
def solution(new_id):
    answer = ''
    cnt = 0
    i = 0
    new_id_1 = new_id.lower()
    while i < len(new_id_1):
        if new_id_1[i].isalpha() == False and new_id_1[i] != '.' and new_id_1[i] != '-' and new_id_1[i] != '_' and new_id_1[i].isdigit() == False:
            new_id_1 = new_id_1[:i] + new_id_1[i+1:]
            i -= 1
        i += 1
    i = 0
    while i < len(new_id_1):
        if new_id_1[i] == '.':
            cnt += 1
            if i == len(new_id_1) - 1:
                if len(new_id_1) >= (i + 1) and cnt >= 2:
                    new_id_1 = new_id_1[:i - cnt + 1] + new_id_1[i:]
                    i = i + 1 - cnt
                    cnt = 0
            elif new_id_1[i + 1] != '.':
                if len(new_id_1) >= (i + 1) and cnt >= 2:
                    new_id_1 = new_id_1[:i - cnt + 1] + new_id_1[i:]
                    i = i + 1 - cnt
                    cnt = 0
                elif cnt == 1:
                    cnt = 0
        i += 1
    if len(new_id_1) != 0:
        if new_id_1[0] == '.':
            new_id_1 = new_id_1[:0] + new_id_1[1:]
    if len(new_id_1) != 0:
        if new_id_1[len(new_id_1)-1] == '.':
            new_id_1 = new_id_1[:len(new_id_1)-1] + new_id_1[len(new_id_1):]

    if new_id_1 == "":
        new_id_1 = new_id_1 + 'a'
    if len(new_id_1) >= 16:
        new_id_1 = new_id_1[0:15]
        if new_id_1[len(new_id_1) - 1] == '.':
            new_id_1 = new_id_1[:len(new_id_1) - 1] + new_id_1[len(new_id_1):]
    if len(new_id_1) <= 2:
        if len(new_id_1) == 2:
            new_id_1 = new_id_1 + new_id_1[len(new_id_1)-1]
        if len(new_id_1) == 1:
            new_id_1 = new_id_1 + new_id_1[len(new_id_1) - 1]
            new_id_1 = new_id_1 + new_id_1[len(new_id_1) - 1]
    answer = new_id_1
    return answer

