n = int(input())

cr, co, br = 0, 0, 0

for i in range(1, n+1):
    if i % 12 == 0:
        br += 1
        # print(f"bathroom:{br}")
    elif i % 3 == 0:
        co += 1
        # print(f"corridor:{co}")
    elif i % 2 == 0:
        cr += 1
        # print(f"classroom:{cr}")
print(cr, co, br)