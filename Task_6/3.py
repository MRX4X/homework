a = {}
b = list()
while True:
    t = input('Трек: ')
    if t == 'off':
        break
    n = input('Имя: ')
    if n == 'off':
        break
    b.append(n)
    plase = input('Место: ')
    if plase == 'off':
        break
    b.append(plase)
    a[tuple(b)] = t
print(a)
