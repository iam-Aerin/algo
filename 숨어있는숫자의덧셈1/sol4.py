def solution(my_string):
    
    numbers = '0123456789'

    for char in my_string:
      #if char 가 숫자인가요?
      if char in numbers:
        answer += int(char)
    
    return answer

# my_string	result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	16

print(solution("aAb1B2cC34oOp"))