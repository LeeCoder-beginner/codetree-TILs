n = int(input())

# 정삼각형 n개 출력
for i in range(n):
    for j in range(n-i-1): # 공백 출력1
        print(" ", end="")
    
    for j in range((2*i)+1): # 별 출력1
        print("*", end="")

    print()
    
# 뒤집어진 정삼각형 n-1개 출력
for i in range(n-1):
    for j in range(i+1): # 공백 출력 2
        print(" ", end="")

    for j in range((2*n)-(2*i)-3): # 별 출력 2
        print("*", end="")

    print()