testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
a=set()
b=True
for i in testList:
    if ((type(i) == set or type(i) == dict or type(i) == list)):
        b=False
for i in testList:
    if (not (type(i) == set or type(i) == dict or type(i) == list)):
        a.add(i)
print(b, a)