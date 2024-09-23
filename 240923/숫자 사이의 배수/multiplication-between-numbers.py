a, b = map(int, input().split())
sum_val = 0
ave_val = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1
ave_val = sum_val / cnt

print(f"{sum_val} {ave_val:.1f}")