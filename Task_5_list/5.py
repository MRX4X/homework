numbers = []
b = numbers.sort()
while True:
    a = int(input())
    d = print('Вы хотите продолжить? Если да - введите 0')
    n = int(input())
    if n == 0:
        print('Продолжайте')
        numbers.append(a)
    else:
        break
print(numbers)
print(b)
if numbers == b:
    print('Да')
else:
    print('Нет')

