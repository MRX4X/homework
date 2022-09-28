a=int(input())
b=int(input())
c=int(input())
d=a+b+c
if b>a and c>b:
    print('Акция', d//2)
elif a>b and b>a:
    print('Акция', d//3)
else:
    print('К оплате:', d)