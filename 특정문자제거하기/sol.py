# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
# my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):
    answer = ''
    
    answer = my_string.replace(letter, '')
    return answer

replace(old, new, -1)의 의미는?
# count 값이 **음수(-1)**이면, 
# 모든 old를 new로 변경하는 것과 동일합니다.
# my_string	letter	result

# "abcdef"	"f"	"abcde"
# "BCBdbe"	"B"	"Cdbe"

