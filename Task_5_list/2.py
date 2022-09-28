numbers=[]
while True:
    a=int(input())
    b = numbers.count(5)
    c = numbers.count(4)
    d = numbers.count(3)
    v = len(numbers)
    if a!=0:
        numbers.append(a)
    else:
        break
print(((b+c+d+v)/v)*100)
