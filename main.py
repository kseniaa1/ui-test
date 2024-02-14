import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTreeView, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import json


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Классическая библиотека")
        if not os.path.exists('put_json_here/classics.json'):
            QMessageBox.warning(self, "Предупреждение", "json файл не найден в своей папке.")
            return
        with open('put_json_here/classics.json', 'r') as file:
            data = json.load(file)

        model = QStandardItemModel()
        self.populate_model(model, data)

        tree_view = QTreeView()
        tree_view.setModel(model)

        layout = QVBoxLayout()
        layout.addWidget(tree_view)
        self.setLayout(layout)

    def populate_model(self, model, data, parent=None):
        if isinstance(data, dict):
            for key, value in data.items():
                item = QStandardItem(str(key))
                if parent is None:
                    model.appendRow(item)
                else:
                    parent.appendRow(item)
                self.populate_model(model, value, item)
        elif isinstance(data, list):
            for i, value in enumerate(data, 1):
                item = QStandardItem(str(i))
                if parent is None:
                    model.appendRow(item)
                else:
                    parent.appendRow(item)
                self.populate_model(model, value, item)
        else:
            item = QStandardItem(str(data))
            if parent is None:
                model.appendRow(item)
            else:
                parent.appendRow(item)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', 'Уже уходите?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
