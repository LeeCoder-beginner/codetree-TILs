# 데이터 받기
arr = list(map(int, input().split()))
sum_double_val = 0
cnt = 0

# 0이 나오기 전까지, 2의 배수와 그 합계를 구한다.
for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        sum_double_val += arr[i]
        cnt += 1

print(cnt, sum_double_val)