# # # 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
# # #만약 정수 10이라면
# # #range(1,11) => 까지의 합을 구해야함. range(10-9, 10+1)
# # # range(5) returns 0, 1, 2, 3, 4
# # # range(n+1) returns 0, 1, 2, ..., n

# # def solution(range(n)):

# #     n=0
# #     answer = 0

# #     for i in n:
# #         print()
    
    
# #     return answer

# # print(solution(1234))

# # # 1234	10
# # # 930211	16

# # n = 1234
# # 1+2+3+4

# n = 930211
# n = str(n)
# 9 + 3 + 0 + 2 + 1 + 1
# print(str(n[0]))

# result = []

# # # 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
# # #만약 정수 10이라면
# # #range(1,11) => 까지의 합을 구해야함. range(10-9, 10+1)
# # # range(5) returns 0, 1, 2, 3, 4
# # # range(n+1) returns 0, 1, 2, ..., n

# def solution(n):

#      n=string(n)

#      result = []
     
#      for i in list(range(:)):
#         result = result + i


#     answer = 0

#     for i in n:
#         print()
    
def solution(n):
    n = str(n)  # 정수를 문자열로 변환
    result = []  # 결과를 저장할 리스트
    
    for i in n:  # 문자열의 각 문자 반복
        result.append(int(i))  # 숫자로 변환 후 리스트에 추가
    
    return sum(result)  # 최종 리스트 반환


# 테스트 실행
print(solution(12345))  # [1, 2, 3, 4, 5]
print(solution(9876))   # [9, 8, 7, 6]
