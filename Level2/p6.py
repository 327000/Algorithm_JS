#카펫
def solution(brown, yellow):
    answer = []
    y_w = 1
    y_h = 1
    b_w = 1
    b_y = 1
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_w = i
            y_h = int(yellow / i)
            if ((y_w + 2) + y_h) * 2 == brown:
                b_w = y_w + 2
                b_h = y_h + 2
                if b_w >= b_h:
                    answer.append(b_w)
                    break

    b_h = int((yellow / y_w)) + 2
    answer.append(b_h)
    print(answer)
    return answer