import sys
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMessageBox, QMainWindow
import json

class MainWindow(QMainWindow):
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение',
            "Вы уверены, что хотите выйти из приложения?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

translation_dict = {
    "Date": "Дата",
    "Data": "Данные",
    "Location": "Локация",
    "Day": "День",
    "Month": "Месяц",
    "Year": "Год",
    "Cases": "Кол-во случаев",
    "Deaths": "Кол-во смертей",
    "Population": "Население",
    "Rate": "Скорость",
    "Country": "Страна",
    "Code": "Код",
    "Continent": "Континент"

}

current_row = 0
def add_json_data(data, parent_item, max_rows):
    global current_row
    if current_row >= max_rows:
        return

    if isinstance(data, dict):
        for key, value in data.items():
            if current_row >= max_rows:
                return

            if key in translation_dict:
                key = translation_dict[key]
            child = QTreeWidgetItem([str(key)])
            parent_item.addChild(child)
            current_row += 1
            add_json_data(value, child, max_rows)
    elif isinstance(data, list):
        for item in data:
            if current_row >= max_rows:
                return

            child = QTreeWidgetItem([''])
            parent_item.addTopLevelItem(child)
            current_row += 1
            add_json_data(item, child, max_rows)
    else:
        parent_item.setText(1, str(data))

with open('covid.json') as file:
    data = json.load(file)

def help():
    max_rows = 10 # Кол-во стран

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    tree_widget = QTreeWidget(main_window)
    tree_widget.setColumnCount(2)
    tree_widget.setColumnWidth(0, 200)
    tree_widget.setHeaderLabels(['Ключ', 'Значение'])
    main_window.resize(600, 400)
    tree_widget.resize(600, 400)

    add_json_data(data, tree_widget, max_rows*14)
    tree_widget.expandAll()
    tree_widget.show()

    main_window.show()

    sys.exit(app.exec())
