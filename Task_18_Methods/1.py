from datetime import datetime
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def Print(self):
        print(self.name, self.age)
    def Gen(cls):
        return Person('Денис', datetime.today().year)
    def staticmeod(self):
        if self.age-datetime.today().year==18:
            return 'Соверщеннолетний'
        else:
            return 'Не соверщеннолетний'

den=Person('Денис', 2008)
print(den.Gen())
print(den.staticmeod())

