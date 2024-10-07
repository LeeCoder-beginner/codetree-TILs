n = int(input())
cnt = 'A'

for i in range(n):
    for j in range(i+1):
        if cnt == 'Z': # 알파벳을 출력하는 경우이기 때문에 Z가 나오면 출력하고 cnt를 A로 바꾸어주는 과정이 필요
            print(cnt, end="") 
            cnt = 'A'
        else:
            print(cnt, end="")
            cnt = chr(ord(cnt) + 1)
    print()