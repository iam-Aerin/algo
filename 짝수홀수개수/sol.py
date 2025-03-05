# 정수가 담긴 리스트 num_list가 주어질 때, 
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ num_list의 길이 ≤ 100
# 0 ≤ num_list의 원소 ≤ 1,000



def solution(num_list):
    even_count = sum(1 for num in num_list if num % 2 == 0)  # 짝수 개수
    odd_count = sum(1 for num in num_list if num % 2 == 1)   # 홀수 개수
    return [even_count, odd_count]

# 테스트 예제
print(solution([1, 2, 3, 4, 5, 6]))  # [3, 3]
print(solution([0, 1, 2, 3, 4]))     # [3, 2]
print(solution([7, 9, 11]))          # [0, 3]
print(solution([2, 4, 6, 8, 10]))    # [5, 0]
