import sys
from math import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.line_input = QLineEdit(self)
        self.line_input.move(5, 5)
        self.line_input.setReadOnly(False)
        font = self.line_input.font()
        font.setPointSize(10)
        self.line_input.setFont(font)
        self.line_input.resize(390, 15)

        self.line_output = QLineEdit(self)
        self.line_output.move(5, 30)
        self.line_output.setReadOnly(True)
        font = self.line_output.font()
        font.setPointSize(10)
        self.line_output.setFont(font)
        self.line_output.resize(390, 15)

        arcsin = QPushButton("arcsin", self)
        arcsin.move(40, 270)
        arcsin.resize(110, 40)
        arcsin.clicked.connect(self.ASin)

        ce = QPushButton("Стереть", self)
        ce.move(280, 40)
        ce.resize(110, 40)
        ce.clicked.connect(self.CE)

        equals = QPushButton("Вычислить", self)
        equals.move(280, 270)
        equals.resize(110, 40)
        equals.clicked.connect(self.Equal)

        c = QPushButton("C", self)
        c.move(10, 40)
        c.resize(112, 40)
        c.clicked.connect(self.C)

        minus = QPushButton("-", self)
        minus.move(160, 270)
        minus.resize(110, 40)

        zero = QPushButton("0", self)
        zero.move(5, 230)
        zero.resize(45, 40)

        one = QPushButton("1", self)
        one.move(5, 180)
        one.resize(45, 40)

        two = QPushButton("2", self)
        two.move(60, 180)
        two.resize(45, 40)

        three = QPushButton("3", self)
        three.move(115, 180)
        three.resize(45, 40)

        four = QPushButton("4", self)
        four.move(5, 130)
        four.resize(45, 40)

        five = QPushButton("5", self)
        five.move(60, 130)
        five.resize(45, 40)

        six = QPushButton("6", self)
        six.move(115, 130)
        six.resize(45, 40)

        seven = QPushButton("7", self)
        seven.move(5, 80)
        seven.resize(45, 40)

        eight = QPushButton("8", self)
        eight.move(60, 80)
        eight.resize(45, 40)

        nine = QPushButton("9", self)
        nine.move(115, 80)
        nine.resize(45, 40)

        point = QPushButton(".", self)
        point.move(115, 230)
        point.resize(45, 40)
        point.clicked.connect(self.Point)

        plus = QPushButton("+", self)
        plus.move(170, 230)
        plus.resize(45, 40)

        multiply = QPushButton("*", self)
        multiply.move(170, 130)
        multiply.resize(45, 40)

        divide = QPushButton("/", self)
        divide.move(170, 80)
        divide.resize(45, 40)

        squared = QPushButton("^", self)
        squared.move(225, 130)
        squared.resize(45, 40)
        squared.clicked.connect(self.Squared)

        root = QPushButton("sqrt", self)
        root.move(225, 80)
        root.resize(80, 40)
        root.clicked.connect(self.Root)


        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        operators = [ce, c, plus, minus, multiply, divide]

        others = [arcsin, squared, root, point]

        for i in nums:
            i.clicked.connect(self.Num)

        for i in operators[2:]:
            i.clicked.connect(self.operator)

        # Window Settings

        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 320)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Уверены?', 'ви таки хотите выйти?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def Num(self):
        self.line_input.setText(self.line_input.text() + self.sender().text())

    def operator(self):
        num = self.line_input.text()
        sender = self.sender()
        operator = sender.text()
        if not (operator == "="):
            self.line_input.setText(self.line_input.text() + self.sender().text())

    def Equal(self):
        newNum = self.line_input.text()
        try:
            output = eval(newNum)
            self.line_output.setText(str(output))
            return True
        except:
            self.line_output.setText('incorrect input')

    def Root(self):
        self.line_input.setText('sqrt(' + self.line_input.text() + ')')

    def Squared(self):
        self.line_input.setText(self.line_input.text() + '**')

    def Point(self):
        if "." not in self.line_input.text(): #сделал бы такую проверку везде, да вот незадачка, степень в питоне - **, а не ^, как у всех нормальных людей
            self.line_input.setText(self.line_input.text() + ".")

    def ASin(self):
        self.line_input.setText('asin(' + self.line_input.text() + ')')

    def CE(self):
        self.line_input.backspace()

    def C(self):
        self.line_input.clear()
        self.line_output.clear()


def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    app.setStyleSheet('QPushButton { background-color: #0d6efd; color: white; font-weight: 600; border-radius: 8px; border: 1px solid #0d6efd; padding: 5px 15px; margin-top: 10px; outline: 0px;}')
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()