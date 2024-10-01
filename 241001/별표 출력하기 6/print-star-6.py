n = int(input())

for i in range(n):
    for j in range(i): # 공백 출력
        print(" ", end=" ")

    for j in range((n*2)-(i*2)-1): # 별 출력1
        print("*", end=" ")

    print()

for i in range(n-1):
    for j in range(n-i-2): # 왜 -2? 처음엔 j에 0이 할당되어 +1을 더 빼줘야 함
        print(" ", end=" ")
    
    for j in range(i*2+3):
        print('*', end=" ")

    print()