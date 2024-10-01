n = int(input())
# 1. 조건에 해당하는 반복문 n개 출력
for i in range(n):
    if i % 2 == 0:
        for j in range((i//2)+1): # i가 짝수일 때, * 수가 늘어남
            print('*', end=" ")
    else:
        for j in range(n-(i//2)): # i가 홀수일 때, * 수가 줄어듦
            print("*", end=" ")
    print()

## 2. 조건에 해당하는 대칭하는 반복문 n개 출력
for i in range(n-1, -1, -1): # i가 -1씩 들어가게 알고리즘 설계
    if i % 2 == 0:
        for j in range((i//2)+1): # i가 짝수일 때, * 수가 줄어듦
            print('*', end=" ")
    else:
        for j in range(n-(i//2)): # i가 홀수일 때, * 수가 늘어남
            print("*", end=" ")
    print()