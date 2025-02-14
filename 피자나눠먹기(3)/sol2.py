def solution(slice, n):
    if n % slice:  # 나머지가 있다면
        return n // slice + 1  # 피자 한 판 추가
    else:
        return n // slice  # 나머지가 없으면 그대로 반환
    