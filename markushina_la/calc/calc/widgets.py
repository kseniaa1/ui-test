import math
import logging

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPushButton, QMessageBox,
)

logging.basicConfig(level=logging.INFO)


class CalcWidget(QWidget):
    def init(self):
        super().init()

        self.init_ui()

    def init_ui(self):

        self.input_line = QLineEdit(self)
        self.result_label = QLabel("Результат: ", self)

        self.btn_add = QPushButton("+", self)
        self.btn_add.clicked.connect(self.calculate_sum)

        self.btn_arctg = QPushButton("arctg", self)
        self.btn_arctg.clicked.connect(self.calculate_arctan)

        btn_calculate = QPushButton("Вычислить", self)
        btn_calculate.clicked.connect(self.calculate_result)

        btn_clear = QPushButton("Стереть", self)
        btn_clear.clicked.connect(self.clear_input)

        layout = QVBoxLayout()
        layout.addWidget(self.input_line)
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_arctg)
        layout.addWidget(btn_calculate)
        layout.addWidget(btn_clear)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_sum(self):
        self.operation = "sum"
        self.update_button_style()

    def calculate_arctan(self):
        self.operation = "arctan"
        self.update_button_style()

    def clear_input(self):
        self.input_line.clear()

    def calculate_result(self):
        try:
            expressions = self.input_line.text().split(',')
            if self.operation == "sum":
                result = sum(eval(expr) for expr in expressions)
                self.result_label.setText(f"Результат сложения: {result}")
            elif self.operation == "arctan":
                expression = expressions[0]
                result = math.degrees(math.atan(float(eval(expression))))
                self.result_label.setText(f"Результат arctg: {result} градусов")
            else:
                self.result_label.setText("Выберите операцию: + или arctg")
        except Exception as e:
            self.result_label.setText(f"Ошибка: {str(e)}")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', 'Вы уверены, что хотите выйти?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def update_button_style(self):
        self.btn_add.setStyleSheet("")
        self.btn_arctg.setStyleSheet("")
        if self.operation == "sum":
            self.btn_add.setStyleSheet("background-color: lightblue")
        elif self.operation == "arctan":
            self.btn_arctg.setStyleSheet("background-color: lightblue")