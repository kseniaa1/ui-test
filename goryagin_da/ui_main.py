import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

def populate_tree(tree, data):
    for item in data:
        location = item["Location"]
        location_node = tree.insert("", "end", text=f"{location['Country']} - {location['Region']}")

        data_node = tree.insert(location_node, "end", text="Location")
        for key, value in item["Location"].items():
            if isinstance(value, dict):
                mag_node = tree.insert(data_node, "end", text=key)
                for sub_key, sub_value in value.items():
                    tree.insert(mag_node, "end", text=f"{sub_key}: {sub_value}")
            else:
                tree.insert(data_node, "end", text=f"{key}: {value}")

        data_node = tree.insert(location_node, "end", text="Data")
        for key, value in item["Data"].items():
            if isinstance(value, dict):
                mag_node = tree.insert(data_node, "end", text=key)
                for sub_key, sub_value in value.items():
                    tree.insert(mag_node, "end", text=f"{sub_key}: {sub_value}")
            else:
                tree.insert(data_node, "end", text=f"{key}: {value}")
def on_closing():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

root = tk.Tk()
root.title("Иерархический список")
root.protocol("WM_DELETE_WINDOW", on_closing)

tree = ttk.Treeview(root)
tree.pack()

data = {}
with open("C:/Users/jenke/Downloads/GTKapp-master/GTKapp-master/coffee.json", "r") as file:
    data = json.load(file)

populate_tree(tree, data)

root.mainloop()
