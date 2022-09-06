# LEVEL_1 : 성격 유형 검사하기
def solution(survey, choices):
    answer = ''
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(0, len(survey)):
        if survey[i][0] == 'R':
            if choices[i] - 4 >= 0:
                dic['T'] += (choices[i] - 4)
            else:
                dic['R'] += (abs(choices[i] - 4))
        if survey[i][0] == 'T':
            if choices[i] - 4 >= 0:
                dic['R'] += (choices[i] - 4)
            else:
                dic['T'] += (abs(choices[i] - 4))
        if survey[i][0] == 'C':
            if choices[i] - 4 >= 0:
                dic['F'] += (choices[i] - 4)
            else:
                dic['C'] += (abs(choices[i] - 4))
        if survey[i][0] == 'F':
            if choices[i] - 4 >= 0:
                dic['C'] += (choices[i] - 4)
            else:
                dic['F'] += (abs(choices[i] - 4))
        if survey[i][0] == 'J':
            if choices[i] - 4 >= 0:
                dic['M'] += (choices[i] - 4)
            else:
                dic['J'] += (abs(choices[i] - 4))
        if survey[i][0] == 'M':
            if choices[i] - 4 >= 0:
                dic['J'] += (choices[i] - 4)
            else:
                dic['M'] += (abs(choices[i] - 4))
        if survey[i][0] == 'A':
            if choices[i] - 4 >= 0:
                dic['N'] += (choices[i] - 4)
            else:
                dic['A'] += (abs(choices[i] - 4))
        if survey[i][0] == 'N':
            if choices[i] - 4 >= 0:
                dic['A'] += (choices[i] - 4)
            else:
                dic['N'] += (abs(choices[i] - 4))

    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer