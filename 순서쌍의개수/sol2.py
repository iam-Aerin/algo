def solution(n):
    answer = 0
    for num in range(1, n+1):
    #1부터 n까지의 범위의 반복문

        if n % num == 0:
            answer += 1

    return answer

print(solution(20))
print(solution(100))