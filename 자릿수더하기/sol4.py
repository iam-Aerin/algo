def solution(n):
    answer = 0


    return sum(map(int, list(str(n))))
    #                           list(글자'1234')
    #                       ['1', '2', '3', '4']
    #                  map(int, ['1', '2', '3', '4'])
    #            [1, 2, 3, 4]
    #       sum[1, 2, 3,4]

print(solution(1234))
print(solution(930211))

