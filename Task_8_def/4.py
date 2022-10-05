def add(weight, heught):
    index=weight/(heught**2)
    return index
def ass(i):
    if i<18.5:
        print('Недостаточный вес')
    elif i>=18.5 and i<=25:
        print('ИМТ в норме')
    else:
        print('Избыточный вес')

i = add(int(input()),int(input()))
ass(i)

