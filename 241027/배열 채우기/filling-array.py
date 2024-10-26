list1 = list(map(int, input().split()))

# 0이 나오기 전까지 저장해주는 list 만들기
list2 = []

for i in range(len(list1)):
    if list1[i] == 0:
        break
    else:
        list2.append(list1[i])

# 0dl 나오기 전까지 저장되어 있는 list를 역순으로 출력하기
for i in range(len(list2)-1, -1, -1):
    print(list1[i], end=" ")