n = int(input())

for i in range(1, n+1):
    for j in range(n-i+1):  # i가 홀수일 때, * 수가 1개씩 줄어듦
        print('*', end=' ')
    print()
    for j in range(i):  # i가 짝수일 때, * 수가 1개씩 늘어남
        print("*", end=" ")
    print()