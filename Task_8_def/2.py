def discaunt(a):
    if a<=49:
        print('Скидка 10%')
    elif a>50 and a<99:
        print('Скидка 15%')
    else:
        print('Скидка 20%')
discaunt(a=int(input()))