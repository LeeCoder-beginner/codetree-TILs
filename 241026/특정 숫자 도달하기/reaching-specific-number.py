lis = list(map(int, input().split()))
sum_val = 0
list1 = []
for i in range(len(lis)):
    if lis[i] >= 250:
        break
    else:
        sum_val += lis[i]
        list1.append(lis[i])

print(sum_val, sum_val/len(list1))