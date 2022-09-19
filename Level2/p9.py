#짝지어 제거하기
def solution(s):
    temp = []
    for i in s:
        if len(temp) == 0:
            temp.append(i)
        elif temp[-1] != i:
            temp.append(i)
        elif temp[-1] == i:
            temp.pop()

    if len(temp) == 0:
        return 1
    else:
        return 0