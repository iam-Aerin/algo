# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = 0

    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]



# numbers = []

#     for number in numbers:    
#         if number == max(numbers):
#             numbers.append(number)
#         elif max(numbers)-number == max

# #가장 큰 수 두개를 뽑아야함.
# #가장 큰 수
# #그리고 뽑은 그 두개의 수를 곱해야함. 

## 넘버 2개를 뽑아서, 그 둘을 곱한 값이 최댓값일 때를 호출한다. 
## (최댓값과 두번째로 큰 값을 호출하지않고)


print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))

