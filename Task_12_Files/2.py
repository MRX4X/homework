with open('test.txt', 'r') as i:
    a=i.read()
f=open('test_2.txt', 'w')
with open('test_2.txt', 'w') as i_1:
    b=i_1.write('но у меня не получается')
with open('test_2.txt', 'r') as i_3:
    c=i_3.read()
f_1=open('test_3.txt', 'w')
with open('test_3.txt', 'w') as i_2:
    i_2.write(a)
    i_2.write(c)
    
