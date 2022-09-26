numbers=[]
while True:
    a=int(input())
    b = numbers.count(a)
    if a!=0:
        if b==0:
            numbers.append(a)
        else:
            print('Эта игра уже записанна')
    else:
        break
print(numbers)
