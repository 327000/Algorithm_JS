# LEVEL_1 : 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1,len(arr)):
        forward = arr[i - 1]

        if i != 0 and arr[i] == forward:
            pass

        else:
            answer.append(arr[i])
    return answer