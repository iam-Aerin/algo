def solution(n):
    answer = 0  # 짝수를 더할 변수 초기화

    for i in range(2, n+1, 2):
        #2칸씩 건너뛰면서
        if i % 2 == 0:  # 짝수인지 확인
            answer = i + answer  # 짝수면 total에 더하기
            # answer += 1

    return answer  # 최종 합 반환

print(solution(10))
print(solution(4))