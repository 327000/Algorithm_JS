# LEVEL_1 : 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    report_1 = list(set(report))
    reported = {}
    mailed = {}
    for i in range(0, len(id_list)):
        mailed[id_list[i]] = 0
    for i in range(0, len(report_1)):
        a, b = report_1[i].split()
        if reported.get(b) == None:
            reported[b] = 1
        else:
            reported[b] += 1
    for i in range(0, len(report_1)):
        a, b = report_1[i].split()
        if reported[b] >= k:
            if mailed[a] == 0:
                mailed[a] = 1
            else:
                mailed[a] += 1
    for _ in mailed:
        if mailed[_] > 0:
            answer.append(mailed[_])
        else:
            answer.append(0)
    return answer