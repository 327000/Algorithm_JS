# LEVEL_1 : 최소 직사각형
def solution(sizes):
    answer = 0
    max_w = sizes[0][0]
    max_h = sizes[0][1]

    for i in range(1, len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            a = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = a

        if max_w >= max_h:
            if max_w < sizes[i][0]:
                max_w = sizes[i][0]
            if max_h < sizes[i][1]:
                max_h = sizes[i][1]

        else:
            if max_h < sizes[i][0]:
                max_h = sizes[i][0]
            if max_w < sizes[i][1]:
                max_w = sizes[i][1]
    answer = max_w * max_h
    return answer