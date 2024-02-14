import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = "Enter a number"
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)