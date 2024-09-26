sum_val = 0
cnt = 0

while True:
    n = int(input())
    if n >= 30 or n <= 19:
        break
    
    sum_val += n
    cnt += 1

a = sum_val / cnt
print(f"{a:.2f}")