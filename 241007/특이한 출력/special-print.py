n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i+j) % 4 == 0: # i+j가 4의 배수가 되는 조건문 설정
            print(f"{i, j}")
        else:
            print(f"{i, j}", end=" ")