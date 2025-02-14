# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 
# 4를 return하도록 solution 함수를 완성해주세요.

예각 : 0 < angle < 90
직각 : angle = 90
둔각 : 90 < angle < 180
평각 : angle = 180

def solution(angle):
    answer = 0
        if 0 < angle < 90:
            return 1
        elif angle =+ 90:
            return 2
        elif 90 < angle < 180:
            return 3
        else 
            return 4



    return answer

print(solution(70))
print(solution(180))


def solution(angle):
    if 0 < angle < 90:  # 예각
        return 1
    elif angle == 90:    # 직각
        return 2
    elif 90 < angle < 180:  # 둔각
        return 3
    elif angle == 180:   # 평각
        return 4

# 테스트 예제 실행
print(solution(70))   # 1 (예각)
print(solution(90))   # 2 (직각)
print(solution(120))  # 3 (둔각)
print(solution(180))  # 4 (평각)
