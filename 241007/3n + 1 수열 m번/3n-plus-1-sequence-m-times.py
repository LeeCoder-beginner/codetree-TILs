m = int(input())

for i in range(m):
    n = int(input())
    cnt = 0         # cnt 초기화
    while True:     # # 무한 루프 생성
        if n == 1:  # n이 1일 경우, 반복문을 나오는 조건문 설정
            break
        elif n % 2 == 1: # n이 홀수일 경우 3n+1 조건문 설정
            n = (n*3)+1
            cnt += 1
        else:           # n이 짝수일 경우 n//2 조건문 설정 
            n //= 2
            cnt += 1
            

    print(cnt)