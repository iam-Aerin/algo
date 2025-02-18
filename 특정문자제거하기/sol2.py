def solution(my_string, letter):
    answer = ''
    
    for char in my_string:
        if char != letter:
            answer = answer + char
          answer = '' (초기값)
            # 첫 번째 문자 'a' → 'c'가 아니므로 answer = '' + 'a' → 'a'
            # 두 번째 문자 'b' → 'c'가 아니므로 answer = 'a' + 'b' → 'ab'
            # 세 번째 문자 'c' → 'c'이므로 건너뜀
            # 네 번째 문자 'd' → 'c'가 아니므로 answer = 'ab' + 'd' → 'abd'
            # 다섯 번째 문자 'e' → 'c'가 아니므로 answer = 'abd' + 'e' → 'abde'
            # 결과적으로 'c'가 제거된 'abde'가 반환됩니다.
    
    return answer


# my_string	letter	result
# "abcdef"	"f"	"abcde"
# "BCBdbe"	"B"	"Cdbe"

