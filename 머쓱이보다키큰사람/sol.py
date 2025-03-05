머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

array	height	result
[149, 180, 192, 170]	167	3
[180, 120, 140]	190	0

입출력 예 #1
149, 180, 192, 170 중 머쓱이보다 키가 큰 사람은 180, 192, 170으로 세 명입니다.

입출력 예 #2
180, 120, 140 중 190보다 큰 수는 없으므로 0명입니다.


어떠한 키 값이 있을 때, 이것보다 큰 데이터의 개수를 세야함. 그리고 그걸  RETURN 



#1 문제풀이
def solution(array, height):
    return sum(1 for num in array if num > height)  # 조건을 만족하는 요소의 개수를 합산

# 테스트 예제
print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))  # 0


#2 문제풀이 
def solution(array, height):
    return len([num for num in array if num > height])  # 키 큰 사람만 리스트로 만들고 길이 반환

# 테스트 예제
print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))  # 0

#3 문제풀이

def solution(array, height):
    count = 0  # 키가 큰 사람의 수를 저장할 변수 초기화
    for num in array:  # 리스트를 순회하면서
        if num > height:  # 머쓱이보다 키가 크다면
            count += 1  # 카운트 증가
    return count  # 최종 개수 반환

# 테스트 예제
print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))  # 0

sides	result
[1, 2, 3]	2
[3, 6, 2]	2
[199, 72, 222]	1
입출력 예 설명
입출력 예 #1

가장 큰 변인 3이 나머지 두 변의 합 3과 같으므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.
입출력 예 #2

가장 큰 변인 6이 나머지 두 변의 합 5보다 크므로 삼각형을 완성할 수 없습니다. 따라서 2를 return합니다.
입출력 예 #3

가장 큰 변인 222가 나머지 두 변의 합 271보다 작으므로 삼각형을 완성할 수 있습니다. 따라서 1을 return합니다.