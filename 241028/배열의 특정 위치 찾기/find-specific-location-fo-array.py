# 입력값을 받을 변수 지정
arr = list(map(int, input().split()))

# 짝수 번째로 입력된 값의 합과 3의 배수 번째로 입력된 값의 평균을 구한다
sum_list = arr[1::2]
ave_list = arr[2::3]

# print(sum_list)
# print(ave_list)
print(sum(sum_list), end=" ")
print(f"{sum(ave_list) / len(ave_list)}")