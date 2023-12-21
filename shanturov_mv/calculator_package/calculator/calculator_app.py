import math
import tkinter as tk
import argparse
from tkinter import messagebox

from custom_button import CustomButton
from entry_with_placeholder import EntryWithPlaceholder


class CalculatorApp(tk.Tk):
    def __init__(self, logging=False):
        tk.Tk.__init__(self)
        self.title("Калькулятор")

        self.entry = EntryWithPlaceholder(self)
        self.entry.grid(row=0, column=0, columnspan=3)

        self.output = tk.Entry(self, state="disabled")
        self.output.grid(row=1, column=0, columnspan=3)

        self.btn_clear = CustomButton(self, text="Стереть", command=self.clear, bg="lightblue")
        self.btn_clear.grid(row=2, column=1)

        self.btn_cosh = CustomButton(self, text="cosh", command=self.cosh, bg="lightblue")
        self.btn_cosh.grid(row=3, column=0)

        self.btn_calculate = CustomButton(self, text="Вычислить", command=self.calculate, bg="lightblue")
        self.btn_calculate.grid(row=3, column=2)

        self.btn_multiply = CustomButton(self, text="Умножить", command=self.multiply, bg="lightblue")
        self.btn_multiply.grid(row=4, column=0, columnspan=3)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.logging = logging

    def multiply(self):
        x = float(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(x) + " * ")
        self.first_num = x
        self.op = "multiply"

    def cosh(self):
        x = float(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "cosh(" + str(x) + ")")
        result = math.cosh(x)
        self.output.config(state="normal")
        self.output.delete(0, tk.END)
        self.output.insert(tk.END, " = " + str(result))
        self.output.config(state="disabled")

    def clear(self):
        self.entry.delete(0, tk.END)
        self.output.config(state="normal")
        self.output.delete(0, tk.END)
        self.output.config(state="disabled")

    def calculate(self):
        if self.op == "multiply":
            y = float(self.entry.get().split("*")[1])
            result = self.first_num * y
            self.output.config(state="normal")
            self.output.delete(0, tk.END)
            self.output.insert(tk.END, " = " + str(result))
            self.output.config(state="disabled")

    def on_closing(self):
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.destroy()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logging", action="store_true", help="Enable logging of user actions")
    args = parser.parse_args()

    app = CalculatorApp(args.logging)
    app.mainloop()


if __name__ == '__main__':
    main()