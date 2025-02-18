def solution(my_string):
    
    for char in my_string:
     if not (ord('A') <= ord(char) <= ord('z')):
        answer += int(char)
     #not(ord를 통해 ASCII CODE에 따라 글자만을 골라오는 작업)
     # => 숫자인가요?
     #if 65 <= ord(char) <= 90

    return answer


# my_string	result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	16

print(solution("aAb1B2cC34oOp"))