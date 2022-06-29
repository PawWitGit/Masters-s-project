from calendar import Calendar
import tkinter as tk
from tkinter import CENTER, NW, Button, Canvas, Label, ttk
from tkinter.messagebox import showinfo

# from matplotlib.ft2font import HORIZONTAL
from tkcalendar import *

from click import style


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        style = SetStyle()
        self.title("My app")
        self.config(height=500, width=550)

        self.can = Canvas(height=400, width=800)
        self.can.grid(columnspan=3, rowspan=4)

        self.info_label = Label(
            text="Wybierz daty początku i końca filtrowania",
            font=(style.font_style(), 13),
        )
        self.info_label.grid(column=1, row=0)

        self.sep_line_1 = ttk.Separator(orient="vertical").grid(
            column=1, row=1, sticky="ns", rowspan=3
        )

        self.start_date_label = Label(
            text="Poniżej wybierz\ndatę początkową", font="12"
        )
        self.start_date_label.grid(column=0, row=1)

        self.end_date_label = Label(text="Poniżej wybierz\ndatę końcową", font="12")
        self.end_date_label.grid(column=2, row=1)

        self.plot_button = tk.Button(
            text="Pokaż wykres",
            font=style.font_style(),
            bg=style.btn_bg_style(),
            fg=style.btn_fg_style(),
            height=3,
            width=13,
        )
        self.plot_button.grid(column=1, row=2)

        self.start_date = Calendar()
        self.start_date.grid(column=0, row=2)

        self.end_date = Calendar()
        self.end_date.grid(column=2, row=2)


class SetStyle:
    def __init__(self) -> None:
        pass

    @staticmethod
    def btn_bg_style():
        bg = "#91BE7B"
        return bg

    @staticmethod
    def btn_fg_style():
        bg = "#000000"
        return bg

    @staticmethod
    def font_style():
        font = "Raleway"
        return font


if __name__ == "__main__":
    app = App()
    app.mainloop()
