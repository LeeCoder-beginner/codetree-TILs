n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

# # 1. for j문의 조건이 위와 동일한 경우
# for i in range(n-2, -1, -1):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# 2. 직각삼각형  for문
for i in range(n-1):
    for j in range(i+2):
        print("*", end=" ")
    print()