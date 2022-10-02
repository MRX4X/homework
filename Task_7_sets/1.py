list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]
a=set(list1)
b=set(list2)
z = list(a.intersection(b))
z.sort()
print(z)
