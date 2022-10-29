a=input()
with open(a, 'r') as i:
    c=i.read()
    print(c)
with open('test_4.txt', 'w') as f:
    f.write('1: ')
    f.write(c)
