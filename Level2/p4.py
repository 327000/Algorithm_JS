#최솟값 만들기
def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    for i in range(len(A)):
        answer = answer + A[i] * B[len(A) - 1 - i]

    return answer