numbers=[]
while True:
    a=int(input())
    b = numbers.count(5)
    v = len(numbers)
    if a!=0:
        numbers.append(a)
    else:
        break
print((b*100)/v)
