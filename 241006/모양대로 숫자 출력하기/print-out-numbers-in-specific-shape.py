n = int(input())

for i in range(n):
    for j in range(i):          # 공백은 i가 1 증가할수록 공백이 1 증가
        print(" ", end=" ")
    for j in range(n): # *은 i가 1 증가할수록 * 1씩 감소
        print(n-j, end=" ")
    n -= 1
    print()