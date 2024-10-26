# 입력을 받을 변수 지정
n = int(input())

# 통과한 학생 수를 세는데 필요한 변수 지정
cnt = 0

# 각 학생의 시험 점수 총합을 계산 / 60점이면 pass와 cnt 누적, 미만이면 fail를 출력
for i in range(n):
    sum_val = 0 # 평균 계산 변수 지정(초기화과 필요)
    test = list(map(int, input().split()))
    for j in range(4):
        sum_val += test[j]
    if sum_val/4 >= 60:
        print('pass')
        cnt += 1
    else:
        print("fail")

print(cnt)