import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QDialog, \
    QDialogButtonBox, QFormLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ввод значения")

        self.value_field = QLineEdit()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow("Значение:", self.value_field)
        layout.addWidget(button_box)

        self.setLayout(layout)


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 400, 400)

        # Создаем основной виджет и компоновщик
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Создаем строки ввода и вывода
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите число и операцию")
        layout.addWidget(self.input_field)

        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)
        layout.addWidget(self.result_field)

        # Создаем кнопки для операций
        buttons = [
            QPushButton("arccos"),
            QPushButton("-"),
            QPushButton("стереть"),
            QPushButton("вычислить")
        ]

        for button in buttons:
            button.setStyleSheet("background-color: lightblue")  # Устанавливаем светло-синий цвет фона кнопок
            button.setMaximumWidth(100)  # Устанавливаем максимальную ширину кнопок

        # Создаем компоновщик для кнопок
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(buttons[0])  # arccos
        buttons_layout.addWidget(buttons[1])  # -
        buttons_layout.addWidget(buttons[2])  # стереть
        buttons_layout.addWidget(buttons[3])  # вычислить

        # Располагаем кнопки по центру
        buttons_layout.addStretch(1)

        layout.addLayout(buttons_layout)

        self.setCentralWidget(widget)

        # Подключаем обработчики событий для кнопок
        buttons[0].clicked.connect(lambda: self.buttonClicked("arccos"))
        buttons[1].clicked.connect(lambda: self.buttonClicked("-"))
        buttons[2].clicked.connect(lambda: self.buttonClicked("стереть"))
        buttons[3].clicked.connect(lambda: self.buttonClicked("вычислить"))

    def buttonClicked(self, text):
        try:
            if text == "вычислить":
                result = eval(self.input_field.text())
                self.result_field.setText(str(result))
            elif text == "стереть":
                self.input_field.setText("")
                self.result_field.setText("")
            elif text == "arccos":
                dialog = InputDialog(self)
                if dialog.exec():
                    value = float(dialog.value_field.text())
                    if -1 <= value <= 1:
                        result = math.acos(math.radians(value))
                        self.result_field.setText(str(result))
                    else:
                        self.result_field.setText("Ошибка: значение должно быть от -1 до 1")
            elif text == "-":
                self.input_field.setText(self.input_field.text() + " - ")
        except Exception as e:
            self.result_field.setText("Ошибка: " + str(e))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы уверены, что хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# Создаем приложение и главное окно
app = QApplication([])
window = CalculatorWindow()
window.show()

# Запускаем главный цикл приложения
app.exec()