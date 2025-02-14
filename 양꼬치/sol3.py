#토탈 계산을 먼저 하고 거기서, 서비스만큼의 가격을 빼는 문제 해설

def solution(n, k):
    #n : 양꼬치 인분수 / k : 음료수 개수
    answer = 0
    #       양꼬치 총액     음료수 총액     서비스음료수가격
    answer = (12000 * n) + (2000 * k) - (n//10 * 2000)

    return answer
    
print(solution(10, 3))
print(solution(64, 6))