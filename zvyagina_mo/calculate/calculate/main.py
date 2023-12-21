from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QGridLayout
import math
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Title')
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.input_display = QLineEdit()
        self.output_display = QLineEdit()
        self.output_display.setReadOnly(True)

        grid.addWidget(QLabel("Ввод:"), 0, 0, 1, 2)
        grid.addWidget(self.input_display, 1, 0, 1, 2)
        grid.addWidget(QLabel("Вывод:"), 2, 0, 1, 2)
        grid.addWidget(self.output_display, 3, 0, 1, 2)

        buttons = {
            "Стереть": self.erase,
            "e^x": self.exp,
            "/": self.divide,
            "Вычислить": self.calculate,
        }

        positions = [(5, 1), (6, 0), (7, 1), (6, 2)]
        for position, (name, handler) in zip(positions, buttons.items()):
            btn = QPushButton(name)
            btn.clicked.connect(handler)
            grid.addWidget(btn, *position)

        self.setLayout(grid)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение',
                                     "Вы уверены, что хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def erase(self):
        self.input_display.clear()
        self.output_display.clear()

    def exp(self):
        try:
            value = float(self.input_display.text())
            result = math.exp(value)
            self.output_display.setText(str(result))
        except ValueError:
            self.output_display.setText("Ошибка ввода")

    def divide(self):
        try:
            values = self.input_display.text().split('/')
            result = float(values[0]) / float(values[1])
            self.output_display.setText(str(result))
        except ValueError:
            self.output_display.setText("Ошибка ввода")
        except ZeroDivisionError:
            self.output_display.setText("Ошибка: деление на ноль")

    def calculate(self):
        try:
            result = eval(self.input_display.text())
            self.output_display.setText(str(result))
        except Exception:
            self.output_display.setText("Ошибка вычисления")

if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())