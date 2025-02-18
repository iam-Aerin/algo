# # 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 
# # 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.

# def solution(num1, num2):
#     answer = divmod((num1/num2)*1000)
# print(answer[0])


#     #num1 / num2
#     #(num1 / num2) * 1000
#     #정수 부분만을 가져오기 divmod((num1/num2)*1000)) => a[0]


#     return answer


# print(solution(num1, num2))
# # num1	num2	result
# # 3	2	1500
# # 7	3	2333
# # 1	16	62



def solution(num1, num2):
    answer = divmod((num1 / num2) * 1000, 1)  # divmod 사용
    #x를 1로 나눈 몫(정수 부분)과 나머지(소수 부분)를 반환
    return int(answer[0])  # 몫(정수 부분)만 반환

# 테스트 실행
print(solution(3, 2))  # 1500
print(solution(7, 3))  # 2333
print(solution(1, 4))  # 250
