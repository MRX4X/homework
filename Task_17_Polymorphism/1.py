class Utka():
    def Kracat(self):
        print('Утка крякает')
    def Nosit_odejdy(self):
        print('Носит одежду')
class Chelovek():
    def Kracat(self):
        print('Имитирует кряканье')
    def Nosit_odejdy(self):
        print('Человек носит одежду')

f1=Utka()
f2=Chelovek()
for i in (f1, f2):
    i.Kracat()
    i.Nosit_odejdy()