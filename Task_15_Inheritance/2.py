class First:
    def __init__(self, name='Денис', genii='гений'):
        self.name=name
        self.genii=genii
class Two(First):
    def Gen_2(self):
        print(self.name+self.genii+"но его отчислят если он не будет учить ООП")

f1=Two()
f1.Gen_2()
