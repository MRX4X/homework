from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count=0
        self.temp = 0
        self.setWindowTitle('Калькулятор')
        self.setGeometry(0, 0, 500, 500)

        self.button_1=QPushButton('1', self)
        self.button_1.setGeometry(140, 300,70,70)
        self.button_1.clicked.connect(self.button_1_was_cliced)

        self.button_2 = QPushButton('2', self)
        self.button_2.setGeometry(210, 300, 70, 70)
        self.button_2.clicked.connect(self.button_2_was_cliced)

        self.button_3 = QPushButton('3', self)
        self.button_3.setGeometry(280, 300, 70, 70)
        self.button_3.clicked.connect(self.button_3_was_cliced)

        self.button_4 = QPushButton('4', self)
        self.button_4.setGeometry(140, 230, 70, 70)
        self.button_4.clicked.connect(self.button_4_was_cliced)

        self.button_5 = QPushButton('5', self)
        self.button_5.setGeometry(210, 230, 70, 70)
        self.button_5.clicked.connect(self.button_5_was_cliced)

        self.button_10 = QPushButton('+', self)
        self.button_10.setGeometry(350, 370, 70, 70)
        self.button_10.clicked.connect(self.button_plus_was_cliced)

        self.button_6 = QPushButton('6', self)
        self.button_6.setGeometry(280, 230, 70, 70)
        self.button_6.clicked.connect(self.button_6_was_cliced)

        self.button_7 = QPushButton('7', self)
        self.button_7.setGeometry(140, 160, 70, 70)
        self.button_7.clicked.connect(self.button_7_was_cliced)

        self.button_8 = QPushButton('8', self)
        self.button_8.setGeometry(210, 160, 70, 70)
        self.button_8.clicked.connect(self.button_8_was_cliced)

        self.button_9 = QPushButton('9', self)
        self.button_9.setGeometry(280, 160, 70, 70)
        self.button_9.clicked.connect(self.button_9_was_cliced)

        self.button_0 = QPushButton('0', self)
        self.button_0.setGeometry(210, 370, 70, 70)
        self.button_0.clicked.connect(self.button_0_was_cliced)

        self.button_11 = QPushButton('-', self)
        self.button_11.setGeometry(350, 300, 70, 70)
        self.button_11.clicked.connect(self.button_minus_was_cliced)

        self.button_12 = QPushButton('=', self)
        self.button_12.setGeometry(280, 370, 70, 70)
        self.button_12.clicked.connect(self.button_equals_was_cliced)

        self.button_13 = QPushButton('🆑', self)
        self.button_13.setGeometry(70, 160, 70, 70)
        self.button_13.clicked.connect(self.button_clear_was_cliced)

        # self.button_14 = QPushButton('Clear_1', self)
        # self.button_14.setGeometry(350, 100, 70, 60)
        # self.button_14.clicked.connect(self.button_clear_1_was_cliced)

        self.button_15 = QPushButton('×', self)
        self.button_15.setGeometry(350, 230, 70, 70)
        self.button_15.clicked.connect(self.button_multiply_was_cliced)

        self.button_16 = QPushButton('÷', self)
        self.button_16.setGeometry(350, 160, 70, 70)
        self.button_16.clicked.connect(self.button_divide_was_cliced)

        self.button_17 = QPushButton('^2', self)
        self.button_17.setGeometry(70, 300,70,70)
        self.button_17.clicked.connect(self.button_cvadrat_was_cliced)

        self.button_18 = QPushButton('√', self)
        self.button_18.setGeometry(70, 230, 70, 70)
        self.button_18.clicked.connect(self.button_coren_was_cliced)

        self.button_19 = QPushButton('< >', self)
        self.button_19.setGeometry(70, 370, 70, 70)
        self.button_19.clicked.connect(self.button_menshe_was_cliced)

        self.lable = QLineEdit(self)
        self.lable.setGeometry(10, 30, 480, 50)


    def button_1_was_cliced(self):
        self.lable.setText(self.lable.text()+'1')

    def button_2_was_cliced(self):
        self.lable.setText(self.lable.text() + '2')

    def button_3_was_cliced(self):
        self.lable.setText(self.lable.text() + '3')

    def button_4_was_cliced(self):
        self.lable.setText(self.lable.text() + '4')

    def button_5_was_cliced(self):
        self.lable.setText(self.lable.text() + '5')

    def button_6_was_cliced(self):
        self.lable.setText(self.lable.text() + '6')

    def button_7_was_cliced(self):
        self.lable.setText(self.lable.text() + '7')

    def button_8_was_cliced(self):
        self.lable.setText(self.lable.text() + '8')

    def button_9_was_cliced(self):
        self.lable.setText(self.lable.text() + '9')

    def button_0_was_cliced(self):
        self.lable.setText(self.lable.text() + '0')

    def button_plus_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('+')
        self.lable.clear()
        self.count = 1

    def button_minus_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('-')
        self.lable.clear()
        self.count = 2

    def button_clear_was_cliced(self):
        self.temp = 0
        self.lable.clear()

    # def button_clear_1_was_cliced(self):
    #     self.lable.text([-1])

    def button_multiply_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('×')
        self.lable.clear()
        self.count = 3

    def button_divide_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('÷')
        self.lable.clear()
        self.count = 4

    def button_cvadrat_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('^2')
        self.lable.clear()
        self.count = 5

    def button_coren_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('√')
        self.count = 6

    def button_menshe_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('< >')
        self.lable.clear()
        self.count = 7

    def button_equals_was_cliced(self):
        if self.count==1:
            self.lable.setText(str(int(self.temp)+int(self.lable.text())))

        if self.count==2:
            self.lable.setText(str(int(self.temp)-int(self.lable.text())))

        if self.count==3:
            self.lable.setText(str(int(self.temp)*int(self.lable.text())))

        if self.count==4:
            self.lable.setText(str(int(self.temp)/int(self.lable.text())))

        if self.count==5:
            self.lable.setText(str(int(self.temp) ** int(self.lable.text())))

        if self.count==6:
            self.lable.setText(str(int(self.temp) ** (0.5)))

        if self.count==7:
            if self.lable.setText(str(int(self.temp) < int(self.lable.text()))):
                self.lable.setText('True')
            if self.lable.setText(str(int(self.temp) > int(self.lable.text()))):
                self.lable.setText('False')




apps=QApplication([])
window = Window()
window.show()
apps.exec()


