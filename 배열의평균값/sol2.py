def solution(numbers):
    answer = 0  # sum 대신 다른 변수명 사용
    
    total = 0
    i = 0

    for number in numbers:
        total = number + total  # 값을 더해서 누적
        i = i + 1

    print(total, i)
    
    answer = total / i 

    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))