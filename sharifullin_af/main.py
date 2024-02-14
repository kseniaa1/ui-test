    import sys
    import json
    from PyQt5.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout
    from PyQt5.QtGui import QStandardItemModel, QStandardItem

    class JSONViewer(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Просмотр данных из файла JSON")

            # Создаем модель для иерархического списка
            self.model = QStandardItemModel()

            # Создаем виджет иерархического списка
            self.tree_view = QTreeView()
            self.tree_view.setModel(self.model)

            # Создаем вертикальный layout
            layout = QVBoxLayout()
            layout.addWidget(self.tree_view)

            self.setLayout(layout)

            # Загружаем данные из файла JSON
            self.load_data()

        def load_data(self):
            try:
                with open('cars.json', 'r') as file:
                    data = json.load(file)
                    self.populate_tree_view(data, self.model)
            except FileNotFoundError:
                print("Файл cars.json не найден!")

        def populate_tree_view(self, data, parent_item):
            if isinstance(data, dict):
                for key, value in data.items():
                    key_item = QStandardItem(str(key))
                    parent_item.appendRow(key_item)
                    if isinstance(value, (dict, list)):
                        self.populate_tree_view(value, key_item)
                    else:
                        value_item = QStandardItem(str(value))
                        key_item.appendRow(value_item)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    key_item = QStandardItem(str(i))
                    parent_item.appendRow(key_item)
                    if isinstance(item, (dict, list)):
                        self.populate_tree_view(item, key_item)
                    else:
                        value_item = QStandardItem(str(item))
                        key_item.appendRow(value_item)

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        viewer = JSONViewer()
        viewer.show()
        sys.exit(app.exec_())