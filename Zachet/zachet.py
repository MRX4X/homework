#5 Задача
def reverseLookup(val):
    dict = {1: 3, 2: 5, 3:5}
    mas=[]
    count=0
    for i in dict:
        if dict[i] == val:
            mas.append(i)
    print('С таким значением', *mas, 'ключи')
reverseLookup(5)