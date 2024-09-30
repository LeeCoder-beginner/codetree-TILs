n = int(input())

for i in range(n):
    for j in range(n-i): # 직각삼각형 뒤집어진 모양의 for문
        print('*', end="")
    
    for j in range(i*2): # 공백 for문
        print(" ", end="")
    
    for j in range(n-i): # 역직각삼각형 뒤집어진 모양의 for문
        print("*", end="")
    
    print()