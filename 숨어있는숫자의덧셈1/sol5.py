def solution(my_string):
    answer = 0

    for char in my_string:

        try:
            answer += int(char)
            #글자에 int를 씌우면 error가 남. 
            #error 가 나면 스킵 (except)해.
        except:
            continue

    return answer
    
print(solution("aAb1B2cC34oOp"))