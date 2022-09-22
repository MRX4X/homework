a=float(input()) #ширина поверхности
b=float(input()) #высота окрашивания
c=a*b #площадь окрашивания
d=int(input()) #расход краски
e=c/d #количество литров
s=int(input()) # кол-во литров в банке
x=(e//s)+1 #количество банок
f=int(input()) #процент запаса
v=e/100
n=v*f #литры не испольлй краски
print(round(c, 2))
print(round(e, 2))
print(round(x))
print(round(n, 2))