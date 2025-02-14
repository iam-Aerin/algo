def solution(n):
    answer = 0  # 짝수를 더할 변수 초기화

    for i in range(n + 1):  # 1부터 n까지 반복
        if i % 2 == 0:  # 짝수인지 확인
            answer = i + answer  # 짝수면 total에 더하기
            # answer += 1

    return answer  # 최종 합 반환

print(solution(10))
print(solution(4))