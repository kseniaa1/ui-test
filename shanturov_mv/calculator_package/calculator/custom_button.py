import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)