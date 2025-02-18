def solution(n):
    answer = 0

    for i in str(n):
        answer = answer + int(i)
#두번의 형변환을 시킴. 

    return answer

print(solution(1234))