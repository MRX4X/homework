def reverseLookup(val):
    dict = {1: 3, 2: 5, 3:5}
    count=0
    for i in dict:
        if i in dict.keys():
            if dict[i] == val:
                count+=1
    print('В словаре с таким занчением', count, 'ключей')

reverseLookup(5)