import json
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * #хз почему, но без этого не импортило messagebox

class JsonToTree:

    def __init__(self):
        self.text_list = []
        self.item_list = []

    def append(self, text_list, item):
        for text in text_list:
            self.text_list.append(text)
            self.item_list.append(item)


class View(QtWidgets.QWidget):

    def __init__(self, path):
        super(View, self).__init__()

        self.tree_widget = None
        self.actual_tree = JsonToTree()

        file = open(path)
        data = json.load(file)

        self.tree_widget = QtWidgets.QTreeWidget()
        self.tree_widget.setHeaderLabels(["ключи", "значения"])
        self.tree_widget.header().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        root_item = QtWidgets.QTreeWidgetItem(["Полный список"])
        self.recursive_parser(data, root_item)
        self.tree_widget.addTopLevelItem(root_item)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.tree_widget)

        justforinh = QtWidgets.QGroupBox(path)
        justforinh.setLayout(layout)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.addWidget(justforinh)

        self.setLayout(layout2)

    def recursive_parser(self, data, tree_widget):

        if type(data) == dict:
            for key, val in data.items():
                self.tree_add_row(key, val, tree_widget)
        elif type(data) == list:
            for i, val in enumerate(data):
                key = str(i)
                self.tree_add_row(key, val, tree_widget)

    def tree_add_row(self, key, val, tree_widget):
        text_list = []

        if type(val) == dict or type(val) == list:
            text_list.append(key)
            row_item = QtWidgets.QTreeWidgetItem([key])
            self.recursive_parser(val, row_item)
        else:
            text_list.append(key)
            text_list.append(str(val))
            row_item = QtWidgets.QTreeWidgetItem([key, str(val)])

        tree_widget.addChild(row_item)
        self.actual_tree.append(text_list, row_item)


class JsonToTreeParser(QtWidgets.QMainWindow):
    def __init__(self):
        super(JsonToTreeParser, self).__init__()

        path = ('D:/Dataset/tate.json')
        window = View(path)

        self.setCentralWidget(window)
        self.setWindowTitle("оно вроде работает")
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Уверены?', 'ви таки хотите выйти?',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    qt_app = QtWidgets.QApplication(sys.argv)
    object = JsonToTreeParser()
    sys.exit(qt_app.exec_())


if "__main__" == __name__:
    main()