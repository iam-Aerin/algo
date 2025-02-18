def solution(n):
    answer = 0

    while n > 0:
        #n이 0일때까지 계속 나눠
        a, b = divmod(n, 10) # (a, b) = divmod(n, 10)
        #n을 10으로 나눈 몫과 나머지가 하나로 묶여서 나오게 된다. 
        a = divmod(n, 10)[0] # n // 10
        b = divmod(n, 10)[1] # n % 10
        #print(1234//10)
        #print(1234%10)

        #나머지를 (누적해서) 더하는 과정이 필요하다. 
        answer = answer + b
        n = a

    return answer

print(solution(1234))
print(solution(930211))

#나머지 연산이 필요함. 
#몫이 0일때까지, 그 누적합을 구할것임. 
#for문은 일정한 범위가 있을때, 작업이 가능함.
#while문을 통해 => 몫이 0이 될때까지
