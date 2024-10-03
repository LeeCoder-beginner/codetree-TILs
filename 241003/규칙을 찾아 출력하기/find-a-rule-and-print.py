n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or j+1 == n or i-1 >= j:
            print('*', end=" ")
        else:
            print(" ", end=" ")

    print()