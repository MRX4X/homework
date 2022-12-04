class Prifile():
    def __init__(self, name, last_name, age_pasport):
        self.name = name
        self.last_name = last_name
        self.age_pasport = age_pasport
    def print_info(self):
        ...
class Address():
    def __init__(self, City, street, zipcode):
        self.City = City
        self.street = street
        self.zipcode = zipcode
class Role():
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked
class BankAccount():
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance
class Order():
    def __init__(self):
        self.item = ''
        self.data = ''
        self.delivery = ''
        self.price = ''

    def Par_order(self, item, data, delivery, price):
        self.item=item
        self.data=data
        self.delivery=delivery
        self.price=price
class User():
    def __init__(self, name, last_name, age_pasport):
        self.profile=Prifile(name, last_name, age_pasport)
        self.adres=[]
        self.role=[]
        self.bankaccount=[]
        self.order=[]
    def addres(self, City, street, zipcode):
        self.adres.append(Address(City, street, zipcode))
    def addrole(self, role, hours_worked):
        self.role.append(Address(role, hours_worked))
    def addbankaccount(self, card_number, balance):
        self.bankaccount.append(BankAccount(card_number, balance))





