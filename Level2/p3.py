#JadenCase 문자열 만들기 (문제병신같음)
def solution(s):
    answer = ''
    s_len = s.split()
    cnt = 0
    i = 0
    while i < len(s):
        if s[i] != ' ':
            a = s.split()[cnt]
            if a[0].isdigit():
                b = a[0]
                for j in range(1, len(a)):
                    if a[j].isupper():
                        b += a[j].lower()
                    else:
                        b += a[j]
                answer += b
                i += len(a)
                cnt += 1
            else:
                c = a.capitalize()
                answer += c
                i += len(a)
                cnt += 1

        else:
            answer += ' '
            i += 1

    return answer