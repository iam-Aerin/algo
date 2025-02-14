def solution(slice, n):
    return n // slice + 1 if n % slice else n // slice

#삼항연산자는 한줄로 작성한다. 
#if n % slice → 나머지가 있으면 한 판 더 추가
#else n // slice → 나머지가 없으면 그대로 반환