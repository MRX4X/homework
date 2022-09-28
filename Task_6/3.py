a = {}
NP = list()
while True:
    track = input('Трек: ')
    if track == 'off':
        break
    name = input('Имя: ')
    if name == 'off':
        break
    NP.append(name)
    plase = input('Место: ')
    if plase == 'off':
        break
    NP.append(plase)
    a[tuple(NP)] = track
print(a)
