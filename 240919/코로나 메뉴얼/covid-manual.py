a_sym, a_tem = input().split()
b_sym, b_tem = input().split()
c_sym, c_tem = input().split()

if a_sym == 'Y' and int(a_tem) >= 37:
    if (b_sym == 'Y' and int(b_tem) >= 37) or (c_sym == 'Y' and int(c_tem) >= 37):
        print("E")
    else:
        print("N")
else:
    if (b_sym == 'Y' and int(b_tem) >= 37) and (c_sym == 'Y' and int(c_tem) >= 37):
        print('E')
    else:
        print("N")