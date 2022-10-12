






































# """Create file with captain's diary."""
#
#
# from datetime import timedelta, date
#
#
# def make_a_file(notes: list, first_note_date: str):
#     """Takes a list with strings - the captain's entries, and the date of the first entry.\
#          Writes notes to a file with dates.
#
#     Args:
#         notes: list - captain's notes
#         first_note_date: str - date of first note like 01.02.2005
#     """
#     one_day = timedelta(days=1)
#
#     note_data = [int(num) for num in first_note_date.split('.')]
#     note_data_right = date(note_data[2], note_data[1], note_data[0])
#
#     file = open('diary', 'w')
#     for note in notes:
#         file.write('\n %s: ' % str(note_data_right))
#         file.write(note)
#
#         note_data_right += one_day
#     file.close()
#
#
# make_a_file(
#     [
#         'В 4 часа 30 минут начали съемку со швартовов и якорей.',
#         'Впереди нас идет флагманская "Сибирь", а за нами "Сахалин". Погода хорошая, видимость \
# полная.', 'За сутки плавания мы еще не вышли из Финского залива. Видимость \
# по-прежнему полная.', '"Сахалин" отделился от нас, пошел в Балтийск.\
# Одновременно в проливах не могут находиться больше трех иностранных\
# военных судов одного флага.', 'Северное, Норвежское и Баренцево \
# моря встретили нас штормом. Техника выдержала.', 'Только в Баренцевом море\
# шторм утихомирился'
#     ],
#     '21.7.2005'
# )






#
# def day():
#     count = 0
#     with open(r"diary", "r") as file:
#         for line in file:
#             count += 1
#     print(count)
# day()
#
# def add(a):
#     mas=[]
#     mas.append(a)
#     f=open(r"diary", "a")
#     for line in mas:
#         f.write(line + '\n')
# add(input())
#
# def dai():
#     count = 0
#     with open(r"diary", "r") as file:
#         for line in file:
#             count += 1
#     print(count)
# dai()

