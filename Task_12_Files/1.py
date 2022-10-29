f=open('test.txt', 'w')
with open('test.txt', 'w') as s:
    s.write("Я гений и стараюсь учить питон")
with open ('test.txt', 'r') as a:
    b=a.read(7)
    print(b)
