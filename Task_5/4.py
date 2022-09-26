numbers=[]
while True:
    a=input()
    b=input()
    c=int(input())
    print('Следущий преподаватель?')
    d=input()
    numbers.insert(0, [a, b, c])
    if d=='да':
        True
    else:
        break
print(numbers)