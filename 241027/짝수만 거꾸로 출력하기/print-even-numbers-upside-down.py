# 입력받은 개수와 수에 대한 변수 지정
n = int(input())
arr = list(map(int, input().split()))

# 짝수를 저장해주고 그 개수를 세주는 변수 지정
even_num = []
cnt = 0

# 반복문을 통해 짝수인지 판별해준다.
for i in range(n):
    if arr[i] % 2 == 0:
        even_num.append(arr[i])
        cnt += 1
    else:
        continue

# 저장된 짝수를 역순으로 출력
for i in range(cnt-1, -1, -1):
    print(even_num[i], end=" ")