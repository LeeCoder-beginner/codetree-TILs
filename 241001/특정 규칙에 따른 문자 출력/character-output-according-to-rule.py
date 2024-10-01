n = int(input())

# 역직각삼각형 다중 for문 n개 출력
for i in range(n):
    for j in range(n-i-1): # 공백 출력 1
        print(" ", end=" ")
    
    for j in range(i+1): # @ 출력 1
        print("@", end=" ")

    print(

    )
# 뒤집어진 직각삼각형 다중 for문 n-1개 출력
for i in range(n):
    for j in range(n-i-1): # @ 출력 2
        print("@", end=" ")
    
    print()