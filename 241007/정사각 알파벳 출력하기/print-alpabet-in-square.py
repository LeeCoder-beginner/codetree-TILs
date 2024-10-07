n = int(input())
letter = 'A'
cnt= 0

for i in range(n):
    for j in range(n):
        print(chr(ord(letter) + cnt), end="")
        cnt += 1
    print()