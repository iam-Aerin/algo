# list comprehension으로 문제 해결하기

def solution(num_list):
    return [len([num for num in num_list if num % 2 == 0]),  # 짝수 개수
            len([num for num in num_list if num % 2 == 1])]  # 홀수 개수
