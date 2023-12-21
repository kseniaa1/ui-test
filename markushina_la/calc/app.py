from PyQt6.QtWidgets import QApplication

from .widgets import CalcWidget


class CalcApp(QApplication):
    def init(self, sys_argv):
        super(CalcApp, self).init(sys_argv)

        self.calc_widget = CalcWidget()
        self.calc_widget.setWindowTitle('Calc')
        self.calc_widget.setGeometry(300, 300, 400, 200)
        self.calc_widget.show()

    def exec(self):
        result = QApplication.exec()
        return result