def solution(array, n):
    count = 0  # 개수를 저장할 변수 초기화
    for num in array:  # 리스트를 순회하면서
        if num == n:  # n과 같은 값이면
            count += 1  # 카운트 증가
    return count  # 최종 개수 반환

# 테스트 예제
print(solution([1, 2, 3, 3, 3, 4, 5], 3))  # 3
print(solution([1, 1, 1, 1], 1))  # 4
print(solution([2, 4, 6, 8], 5))  # 0
