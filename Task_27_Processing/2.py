import multiprocessing

def square(width=5, length=10):
    square_room=width*length
    my_file = open('Красим_стены', 'w+')
    my_file.write('Площадь комнаты: ')
    my_file.write(str(square_room)+'\n')
    print('Площадь комнаты', square_room)

def dye(consumption=5):
    with open('Красим_стены', 'r') as f:
        f.seek(31)
        dye_consumption_read=f.read(2)
    dye_consumption=int(dye_consumption_read)*consumption
    my_file = open('Красим_стены', 'a')
    my_file.write('Расход краски: ')
    my_file.write(str(dye_consumption))


if __name__ == "__main__":

    p1=multiprocessing.Process(target=square())
    p2=multiprocessing.Process(target=dye())
    p1.start()
    p2.start()





# def square(width=5, length=10):
#     square_room=width*length
#     my_file = open('Красим_стены', 'w+')
#     my_file.write('Площадь комнаты: ')
#     my_file.write(str(square_room)+'\n')
#     print('Площадь комнаты', square_room)
# square()
#
# def dye(consumption=5):
#     with open('Красим_стены', 'r') as f:
#         f.seek(31)
#         dye_consumption_read=f.read(2)
#     dye_consumption=int(dye_consumption_read)*consumption
#     my_file = open('Красим_стены', 'a')
#     my_file.write('Расход краски: ')
#     my_file.write(str(dye_consumption))
# dye()