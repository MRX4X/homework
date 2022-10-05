def add():
    while True:
        a = input('Введите имя, или стоп для завершения')
        b=int(input('Введите число предметов'))
        mas=[]
        count=0
        for i in range(b):
            c=int(input('Введите сумму по предмету'))
            mas.append(c)
            count+=1
        sum_1=sum(mas)
        if sum_1>80:
            print('Наградить дипломом.')
        elif sum_1>50 and sum_1<=80:
            print('Наградить похвальной грамотой.')
        else:
            print('Выдать грамоту об участии.')
        if a=='stop':
            print('Прием закончен')
            break
add()