a = {1: [3, 4], 2: [5, 6, 3], 3: [7, 1, 9, 2]}
a[1], a[3] = a[3], a[1]
del a[2]
a['new_key']='new_value'
print(a)
