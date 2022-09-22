a=int(input())
b=int(input())
if b>=8 and b<=22:
    if b>=10 and b<=12:
        print(a//2)
    if b>=20 and b<=22:
        print(a//4)
    else:
        print('Акция не действует в это время')
else:
    print('приходи завтра')