def add():
    a=int(input('Введите число учеников'))
    for i in range(a):
        i=int(input('Балл за финальный тест'))
        if i>50:
            print(True)
        else:
            print(False)
add()














# def add():
#     b=True
#     while True:
#         a=int(input())
#         if a>50:
#             print(b)
#         else:
#             print('Вы отчисленны')
# add()