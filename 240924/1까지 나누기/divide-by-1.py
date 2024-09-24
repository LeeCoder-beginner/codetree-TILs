n = int(input())

# for i in range(1, n+1):
#     n //= i
#     if n <= 1:
#         print(i)
#         break

## 2 while 문
cnt = 0
i = 1

while n > 1:
    n //= i
    i += 1
    cnt += 1
    
print(i-1)