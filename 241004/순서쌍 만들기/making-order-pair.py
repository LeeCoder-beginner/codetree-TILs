n = int(input())

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(f"({i},{j})", end=" ") # {i, j}로 작성시 tuple 구조로 인식하여 , 뒤에 자동으로 띄어쓰기 발생
    print()