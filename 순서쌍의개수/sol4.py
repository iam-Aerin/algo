def solution(n):
    answer = 0  # 초기값을 0으로 변경

    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:  # num이 약수라면
            answer += 2  # 대칭되는 두 개의 약수 추가

            if num * num == n:  # 중복된 약수 방지 (제곱수)
                answer -= 1

    return answer

# 테스트 실행
print(solution(20))   # 6 (약수: 1, 2, 4, 5, 10, 20)
print(solution(100))  # 9 (약수: 1, 2, 4, 5, 10, 20, 25, 50, 100)

# 1️⃣ for num in range(1, int(n ** 0.5) + 1):

# 약수는 대칭을 이루므로, √n까지만 검사하면 됨.
# 예: n=100이면 1~10까지만 확인.
# 2️⃣ if n % num == 0:

# num이 n의 약수라면, n // num도 자동으로 약수!
# 3️⃣ answer += 2

# num과 n // num 두 개의 약수를 추가.
# 4️⃣ if num * num == n:

# 제곱수인 경우(10 × 10 = 100), 중복을 방지하기 위해 answer -= 1.