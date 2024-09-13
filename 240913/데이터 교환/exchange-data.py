a, b, c = 5, 6, 7

# a, b, c = c, a, b

temp1 = b
temp2 = c
b = a
c = temp1
a = temp2

print(a)
print(b)
print(c)