#.sort()
#버블정렬

def solution(numbers):
    n = len(numbers)  # 리스트의 길이

    for i in range(n):  # 전체 리스트를 반복
        for j in range(0, n-i-1):  # 인접한 두 개를 비교
                # j는 인접한 요소를 비교하며 큰 값을 오른쪽으로 이동시키는 역할.
                # 한 번의 i 루프가 끝날 때마다 가장 큰 값이 맨 끝으로 이동함.
                # 따라서, 이미 정렬된 요소는 다시 비교할 필요가 없음 → n-i-1만큼만 비교.
            if numbers[j] > numbers[j+1]:  # 왼쪽 값이 오른쪽 값보다 크다면
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  # Swap (자리 바꿈)
    
    return numbers[-1] * numbers[-2]  # 가장 큰 두 수의 곱 반환

print(solution([1, 2, 3, 4, 5]))   # 20 (4 * 5)
print(solution([0, 31, 24, 10, 1, 9]))  # 744 (24 * 31)

# for 반복문의 동작 과정
# ✅ for i in range(n)
# 리스트의 길이 n만큼 반복 (n-1번까지 정렬하면 됨)
# ✅ for j in range(0, n-i-1)
# j는 0부터 n-i-1까지 반복
# numbers[j]와 numbers[j+1]을 비교하여 
# 더 큰 값이 오른쪽으로 이동하도록 교환


# 개념	설명
# 버블 정렬(Bubble Sort)	인접한 두 개를 비교하여 더 큰 숫자를 오른쪽으로 이동
# for i in range(n)	n-1번 반복하여 정렬
# for j in range(0, n-i-1)	j와 j+1을 비교하며 큰 값을 뒤로 보냄
# if numbers[j] > numbers[j+1]:	숫자가 크면 자리 바꿈 (swap)
# numbers[-1] * numbers[-2]	최댓값 두 개를 곱하여 반환