def solution(my_string):
    
    numbers = []
    #숫자만 빼내서 여기에 저장할 것이라는 빈공간을 생성한다. 

    for char in my_string:
      #if char 가 숫자인가요?
      if char.isdigit():
        #.isdigit이라는 함수로 문제를 풀이함. 
        numbers.append(int(char))

    return sum(numbers)


# my_string	result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	16

print(solution("aAb1B2cC34oOp"))