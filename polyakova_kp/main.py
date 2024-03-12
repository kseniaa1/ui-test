import sys
from PyQt6 import QtWidgets, uic
import math
import logging

logging.basicConfig(level=logging.INFO)


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
        try:
            self.result = math.sin(self.result)
            self.outputLabel.setText(str(self.result))
            logging.info("Sin calculated")
        except  TypeError:
            self.outputLabel.setText("Something is wrong. Clear results")
            logging.error("Invalid operation")
            self.result=0

    def add_value(self):
        if self.inputLineEdit.text() == "":
            new_value = 0
        else:
            new_value = eval(self.inputLineEdit.text())
        try:
            new_value = float(new_value)
            self.result += new_value
            self.outputLabel.setText(str(self.result))
            logging.info("Value added")
        except ValueError:
            self.outputLabel.setText("Something is wrong. Clear results")
            logging.error("Invalid input")
            self.result=0
        except TypeError:
            self.outputLabel.setText("Something is wrong. Clear results")
            logging.error("Invalid operation")
            self.result=0


    def calculate_expression(self):
        expression = self.inputLineEdit.text()
        try:
            if expression == "":
                self.outputLabel.setText(str(0))
            else:
                self.result = eval(expression)
                self.outputLabel.setText(str(self.result))
                logging.info("Expression calculated")
        except Exception as e:
            self.outputLabel.setText("Something is wrong. Clear results")
            logging.error("Error in expression calculation")
            self.result=0

    def clear_values(self):
        self.result = 0
        self.outputLabel.setText("")
        self.inputLineEdit.setText("")
        logging.info("Values cleared")

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Уже уходите?(",
                                                "Вы уверены, что хотите уйти?",
                                                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
            logging.info("Application closed")
        else:
            logging.info("Application was not closed")
            e.ignore()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
