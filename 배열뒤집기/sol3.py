def solution(num_list):
    result = []  # 빈 리스트 생성
    for num in num_list:
        result.insert(0, num)  # 0번째 인덱스에 num 삽입 (역순으로 저장)
    return result

# 테스트
print(solution([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2]))  # [2, 1, 1, 1, 1, 1]
