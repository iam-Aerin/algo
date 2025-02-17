# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
int(my_string)
    for char in my_string:
        if 0 <= char <= 100:
            solution = char + solution
    #my_string 안에 포함되어있는 글자 중 (숫자만 - int 타입의 데이터만) 을 골라내서 더한다. 
    #String 타입의 데이터를 int타입으로 변환해야하지않을까? 
    #그리고 나온 int 타입의 데이터끼리를 더하면 되지 않을까? 

    
    


# my_string	result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	16

print(solution("aAb1B2cC34oOp"))

