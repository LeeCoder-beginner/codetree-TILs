n = int(input())
sum_val = 0
for i in range(1, 101):
    sum_val += i
    if sum_val >= n:
        sum_val -= i
        break

print(sum_val)