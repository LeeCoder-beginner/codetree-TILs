list1 = list(map(int, input().split()))

for i in range(len(list1)-1, -1, -1):
    if list1[i] == 0:
        continue
    else:
        print(list1[i], end=" ")