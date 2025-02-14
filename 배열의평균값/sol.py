# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.


def solution(numbers):
    total = 0  # sum 대신 다른 변수명 사용
    
    for number in numbers:
        total = number + total  # 값을 더해서 누적
    
    answer = total / len(numbers)  # 평균 계산
    
    return answer  # 결과 반환

#원소의 평균값: 다 더해서 나누기 그 원소의 개수
#배열 = list 값값

#     numbers	result
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	5.5
# [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]	94.0

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))