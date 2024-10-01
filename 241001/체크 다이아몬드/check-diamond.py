n = int(input())

# 정삼각형 다중 for문 n개 출력
for i in range(n):
    if i % 2 == 1: # i이 홀수인 경우
        for j in range(n-i-1): # 공백 출력 1
            print(" ", end="")
        for j in range(i+1):   # 별 출력 1
            print("*", end=" ")
    
    elif i % 2 == 0:           # i가 짝수인 경우
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
    
    print()

# 뒤집어진 정삼각형 다중 for문(n-1번 출력)
for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    
    for j in range(n-i-1):
        print("*", end=" ")

    print()