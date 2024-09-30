n = int(input())

for i in range(n):
    for j in range(n-i-1): # 공백 for문
        print(" ", end=" ")
    
    for j in range(i*2+1): # * for문
        print("*", end=" ")
    
    print()