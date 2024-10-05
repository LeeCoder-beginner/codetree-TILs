n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(((n//2)*i*3)+(j+1), end=" ")
    else:
        for j in range(n):
            print((n*((i+(i+1)//2)-1))+(2*j+2), end=" ")
    print()