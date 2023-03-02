import sys
for i in sys.argv:
    print(i)
    if i=="--name":
        print('Oleg')
    if i=='':
        print('Привет мир')