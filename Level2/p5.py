#올바른괄호
def solution(s):
    answer = True
    s_len = len(s)
    o_c = 0
    c_c = 0
    if s_len % 2 != 0:
        return False

    elif s[0] == ')':
        return False

    elif s[s_len - 1] == '(':
        return False

    else:
        for i in range(s_len):
            if s[i] == '(':
                o_c += 1
            else:
                c_c += 1
                if c_c > o_c:
                    return False
        if o_c != c_c:
            return False
