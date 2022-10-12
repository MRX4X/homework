def hex(**kwargs):
    for s, d in kwargs.items():
        print(f'{s}:{d}')
hex(a='hb')




















def add(s):
    stak=[]
    d={'(': ')', '[': ']', '{':'}'}
    for bracket in s:
        if bracket in d:
            stak.append(bracket)
        else:#это закрывающая сокбка
            if len(stak)==0: #нет открывающихся скобок
                return False
            else:
                if d[stak[-1]]==bracket:#проверка на правильность закрытия
                    stak.pop()
                else:
                    return False

