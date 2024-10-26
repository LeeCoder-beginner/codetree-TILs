lis = list(map(float, input().split()))
n = len(lis)
sum_val = 0

for i in range(n):
    sum_val += lis[i]

# ave = lis / n
print(f"{sum_val/n:.1f}")