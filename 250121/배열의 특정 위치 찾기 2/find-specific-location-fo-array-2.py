arr = list(map(int, input().split()))
odd = 0
even = 0

for i in range(10):
    if i % 2 == 0:
        even += arr[i]
    elif i % 2 == 1:
        odd += arr[i]

if odd >= even:
    print(odd - even)
else:
    print(even - odd)
