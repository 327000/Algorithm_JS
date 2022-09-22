#뉴스 클러스터링
def solution(str1, str2):
    str1_dic = {}
    str2_dic = {}

    inter = 0
    tmp_sum = 0
    for i in range(1, len(str1)):
        if str1[i - 1].isalpha() and str1[i].isalpha():
            temp = str1[i - 1].lower() + str1[i].lower()
            if temp in str1_dic:
                a = str1_dic[temp] + 1
                str1_dic[temp] = a
            else:
                str1_dic[temp] = 1

    for i in range(1, len(str2)):
        if str2[i - 1].isalpha() and str2[i].isalpha():
            temp = str2[i - 1].lower() + str2[i].lower()
            if temp in str2_dic:
                a = str2_dic[temp] + 1
                str2_dic[temp] = a
            else:
                str2_dic[temp] = 1

    for i in str1_dic:
        for j in str2_dic:
            if i.lower() == j.lower():
                if str1_dic[i] >= str2_dic[j]:
                    inter += str2_dic[j]
                else:
                    inter += str1_dic[i]
                break

    for i in str1_dic:
        tmp_sum += str1_dic[i]
    for i in str2_dic:
        tmp_sum += str2_dic[i]

    sum_s = tmp_sum - inter
    if sum_s != 0:
        answer = int((inter / sum_s) * 65536)

    else:
        answer = 65536
    return answer