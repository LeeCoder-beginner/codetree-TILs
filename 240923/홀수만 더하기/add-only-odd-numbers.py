n = int(input())
num_val = 0

for i in range(n):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        num_val += num

print(num_val)