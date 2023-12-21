import sys
from PyQt5 import QtWidgets, uic
import math


class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.result = 0
        self.sinButton.clicked.connect(self.calculate_sin)
        self.plusButton.clicked.connect(self.add_value)
        self.calculateButton.clicked.connect(self.calculate_expression)
        self.clearButton.clicked.connect(self.clear_values)

    def calculate_sin(self):
        self.result = math.sin(self.result)
        self.outputLabel.setText(str(self.result))

    def add_value(self):
        if self.inputLineEdit.text() == "":
            new_value = 0
        else:
            new_value = eval(self.inputLineEdit.text())
        try:
            new_value = float(new_value)
            self.result += new_value
            self.outputLabel.setText(str(self.result))
        except ValueError:
            self.outputLabel.setText("Error: Invalid input")

    def calculate_expression(self):
        expression = self.inputLineEdit.text()
        try:
            if expression == "":
                self.outputLabel.setText(str(0))
            else:
                self.result = eval(expression)
                self.outputLabel.setText(str(self.result))
        except Exception as e:
            self.outputLabel.setText("Error: " + str(e))

    def clear_values(self):
        self.result = 0
        self.outputLabel.setText("")
        self.inputLineEdit.setText("")

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Уже уходите?(",
                                                "Вы уверены, что хотите уйти?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

