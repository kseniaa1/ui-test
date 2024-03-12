import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import json


store = Gtk.TreeStore(str)


with open('county_demographics.json') as f:
    json_data = json.load(f)
    json_data = json_data[:50]
def add_items(parent_iter, data):
    if isinstance(data, dict):
        for key, value in data.items():
            iter = store.append(parent_iter, [str(key)])
            add_items(iter, value)
    elif isinstance(data, list):
        for item in data:
            iter = store.append(parent_iter, [""])
            add_items(iter, item)
    else:
        store.append(parent_iter, [str(data)])



root_iter = store.append(None, ["JSON"])
add_items(root_iter, json_data)
view = Gtk.TreeView(model=store)
renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Демография", renderer, text=0)
view.append_column(column)