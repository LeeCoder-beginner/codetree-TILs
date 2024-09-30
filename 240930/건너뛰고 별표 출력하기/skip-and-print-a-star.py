n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    print()

# # 1 2번째 for문의 조건이 같은 경우
# for i in range(n-2, -1, -1):
#     for j in range(i+1):
#         print("*", end="")
#     print()
#     print()

# 2 for문의 조건이 다른경우(직각삼각형 180도 회전)
for i in range(n-1):
    for j in range(n-i-1):
        print("*", end="")
    print()
    print()