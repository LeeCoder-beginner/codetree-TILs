n = int(input())
credit = list(map(float, input().split()))
sum_val = 0
cnt = 0
# 학점 평균 계산
for i in range(n):
    sum_val += credit[i]
    cnt += 1

# 출력(조건) 
cre_ave = sum_val / cnt 

if cre_ave >= 4.0:
    print(f"{cre_ave:.1f}")
    print("Perfect")
elif cre_ave >= 3.0:
    print(f"{cre_ave:.1f}")
    print('Good')
else:
    print(f"{cre_ave:.1f}")
    print('Poor')