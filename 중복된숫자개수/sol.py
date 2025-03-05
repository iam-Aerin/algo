# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때,
#  array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

#  입출력 예
# array	n	result
# [1, 1, 2, 3, 4, 5]	1	2
# [0, 2, 3, 4]	1	0

# 입출력 예 #1
# [1, 1, 2, 3, 4, 5] 에는 1이 2개 있습니다.

# 입출력 예 #2
# [0, 2, 3, 4] 에는 1이 0개 있습니다.




# 숫자 하나를 지정해서 그게 array안에 있는지를 확인해야한다. 
def solution(array, n):
    return array.count(n)  # 리스트의 `count()` 메서드를 사용