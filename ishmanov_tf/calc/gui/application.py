from PyQt6.QtWidgets import QApplication, QMessageBox
from .widgets import Window


class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        window = Window()
        window.show()
        window.exit_this.connect(self.quit)
        self.window = window

    def closeEvent(self, event):
        reply = QMessageBox.question\
        (self, '',
         'Вы уверены, что хотите выйти?',
         QMessageBox.Yes,
         QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
