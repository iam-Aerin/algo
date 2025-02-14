# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면 
# 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

#slice= 2 =< slice =< 10
#최소 한조각 이상 먹는다 = slice - n >= 0

## 12명이 4조각으로 자른 피자를 한 조각 이상씩 먹으려면 최소 3판을 시켜야 합니다.
# => n >= slice * 피자의 개수
#(slice, n)

def solution(slice, n):
    answer = 0
    pizza =  1 
    # pizza 는 최소 1판 부터 시켜야하므로

    while n >= slice * pizza:
        print(solution)


    return pizza

print(solution(7, 10))
print(solution(4, 12))

#print(solution(slice, n)) = 피자의개수
# 7	10	2
# 4	12	3

def solution(slice, n):
    pizza = 1  # 최소 1판은 시켜야 하므로 1부터 시작

    while slice * pizza < n:  # 피자 조각 개수가 사람 수보다 부족하면
        pizza += 1  # 피자 한 판 추가

    return pizza  # 최소 필요한 피자 개수 반환

# 테스트 실행
print(solution(7, 10))  # 2
print(solution(4, 12))  # 3
