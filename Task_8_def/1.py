def add():
    while True:
        a = input('Колледж Сириус, введите - да, чтобы продолжить. Или нет - если закончить')
        b=input('Введите имя:')
        c=input('Введите группу:')
        print("Колледж Сириус. Бейджик готов\n"
              "Имя:",b,"\n"
              "«Группа:", c, "\n"
              "«Готово! Заберите бейджики.")
        if a=='нет':
            break
add()