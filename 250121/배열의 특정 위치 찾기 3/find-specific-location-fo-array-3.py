arr = list(map(int, input().split()))
n = 0
n1 = len(arr)

for i in arr:
    if i == 0:
        n += 1
        break
    else:
        n += 1

print(arr[n-n1-4] + arr[n-n1-3] + arr[n-n1-2])
# print(arr[n1-n-3] + arr[n1-n-2] + arr[n1-n-1])