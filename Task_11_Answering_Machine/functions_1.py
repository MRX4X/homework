def main(a):
    b=['Расп', 'расп', 'Стои', 'стои', 'Тел', 'тел', 'Кур', 'кур', 'Адр', 'адр']
    if b[0] in a or b[1] in a:
        timetable()
    if b[2] in a or b[3] in a:
        price()
    if b[4] in a or b[5] in a:
        info()
    if b[6] in a or b[7] in a:
        courses()
    if b[8] in a or b[9] in a:
        adres()



def timetable():
    print('Распсиание работы зала\nПн - 19:00\nСр - 18:00\nПт - 19:00')
    print('Вы хотите записаться на тренировку? Введите - ДА/НЕТ')
    t1=input()
    s1={}
    if t1=='Да' or t1=='да' or t1=='ДА':
        print('Введите день недели на который хотите записаться')
        t2=input()
        print('Введите удобное время с 8 до 23')
        t3=int(input())
        if 8<t3<23:
            s1[t2]=t3
            print('Вы записанны на', s1)
def price():
    print('К оплате за месяц - 2200')
def info():
    print('Контакты вашего тренера - 8977777777')
def courses():
    print('Подготовительные курсы:\n1.https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjCmbGslOf6AhUPx4sKHa0bClkQFnoECA4QAQ&url=https%3A%2F%2Falmaz-club.ru%2Fsambo-dlja-novichkov%2F&usg=AOvVaw2CAw-3Lkq2-WSenS_Og4UZ\n2.https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjCmbGslOf6AhUPx4sKHa0bClkQFnoECBAQAQ&url=https%3A%2F%2Fxtern.ru%2Fcourses%2Fsambo-fgos&usg=AOvVaw3lhRK8NW5sD1RyJMkKT2Pv')
def adres():
    print('г.Санкт-Петербург, пр.Стачек, д.23')
