n = int(input())

for i in range(1, n+1):
    for j in range(1, n-i+2):
        if (n-i+1) == j:
            print(f"{i} * {j} = {i*j}")
        else:
            print(f"{i} * {j} = {i*j}", end=" ")
            print("/", end=" ")