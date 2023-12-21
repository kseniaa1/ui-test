from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton
)
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from .action import calculate

class Button(QPushButton):
    myclicked = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, *kwargs)
        self.clicked.connect(self._active_mycklicked)

    def _active_mycklicked(self):
        self.myclicked.emit(1)

class Window(QWidget):
    exit_this = pyqtSignal(int)
    def __init__(self, *args, **kwargs):

        self.arr = []

        QWidget.__init__(self, *args, **kwargs)
        container = QVBoxLayout(self)

        self.editFirst = QLineEdit()
        self.editFirst.setPlaceholderText("42*1")
        container.addWidget(self.editFirst)

        self.editSecond = QLineEdit()
        self.editSecond.setPlaceholderText("42")
        container.addWidget(self.editSecond)

        layout = QGridLayout()

        self.erase_button = Button("Стереть")
        self.erase_button.myclicked.connect(self.erase_myclicked)
        layout.addWidget(self.erase_button, 0, 2)

        self.divide_button = Button("/")
        self.divide_button.myclicked.connect(self.divide_myclicked)
        layout.addWidget(self.divide_button, 1, 1)

        self.ctg_button = Button("ctg")
        self.ctg_button.myclicked.connect(self.ctg_myclicked)
        layout.addWidget(self.ctg_button, 2, 0)

        self.result_button = Button("Считать")
        self.result_button.myclicked.connect(self.result_myclicked)
        layout.addWidget(self.result_button, 2, 2)

        container.addLayout(layout)

    @pyqtSlot()
    def erase_myclicked(self):
        self.editFirst.setText("")
        self.editSecond.setText("")

    def divide_myclicked(self):
        self.editFirst.setText(self.editFirst.text()+"/")

    def ctg_myclicked(self):
        self.editFirst.setText(self.editFirst.text()+"ctg")

    def result_myclicked(self):
        self.editSecond.setText(calculate(self.editFirst.text()))

    #
    # def active_myclicked(self):
    #     self.str = self.edit.text()
    #
    #     if self.str != '':
    #         try:
    #             arr = list(map(int, self.str.split(" ")))
    #             self.str = sort(arr)
    #             self.edit.setText("")
    #             self.edit.setPlaceholderText(f"Числа меньше 6: {self.str}")
    #         except Exception:
    #             self.edit.setText("")
    #             self.edit.setPlaceholderText("Введите несколько чисел")