n = int(input())
sum_val = 0
ave_val = 0
cnt = 0

for i in range(n):
    num = int(input())
    sum_val += num
    cnt += 1

ave_val = sum_val / cnt

print(f"{sum_val} {ave_val:.1f}")