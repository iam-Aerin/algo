# 문자열 my_string과 정수 n이 매개변수로 주어질 때, 
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 2 ≤ my_string 길이 ≤ 5
# 2 ≤ n ≤ 10
# "my_string"은 영어 대소문자로 이루어져 있습니다.
# e.g. my_string = "hello"
# n = 3
# print(my_string) = hhheeelllooo

# #include <stdio.h>
# #include <stdbool.h>
# #include <stdlib.h>

# // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
# char* solution(const char* my_string, int n) {
#     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
#     char* answer = (char*)malloc(1);
#     return answer;
# }


def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer = answer + (i * n)

    return answer