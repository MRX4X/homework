class Bank:
    def __init__(self, name, pasport, balance):
        self._name=name
        self.__pasport=pasport
        self.__balance=balance
    def private_1(self):
        return self.__pasport
    def private_2(self):
        return self.__balance
    def smenapasporta(self, parol):
        if parol==666:
            print('Введите новый номер паспорта')
            new_pasport=int(input())
            self.__pasport=new_pasport
            return self.__pasport
    def ismenabalance(self, new_balance):
        if new_balance>0:
            print('Измение баланса')
            self.__balance=new_balance
            return self.__balance
f1=Bank('Денис', 12112, 12)
print(f1.smenapasporta(666))
print(f1.ismenabalance(777))






