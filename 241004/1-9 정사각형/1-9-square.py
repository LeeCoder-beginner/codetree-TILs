n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        if cnt == 10: # cnt이 10이 되는 순간 10으로 나눠주어 1로 변경
            cnt //= 10
            print(cnt, end="")
            cnt += 1
        else:
            print(cnt, end="")
            cnt += 1
    print()