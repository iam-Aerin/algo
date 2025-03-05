def solution(array, n):
    return sum(1 for num in array if num == n)  # n과 같은 값의 개수를 세기

# 테스트 예제
print(solution([1, 2, 3, 3, 3, 4, 5], 3))  # 3
print(solution([1, 1, 1, 1], 1))  # 4
print(solution([2, 4, 6, 8], 5))  # 0
