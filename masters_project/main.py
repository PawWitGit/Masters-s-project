from calendar import Calendar
import tkinter as tk
from tkinter import RAISED, Canvas, Entry, Label, ttk
import datetime as dt

import main_plot
from main_plot import PlotData
from tkcalendar import *


class Gui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        style = SetStyle()

        plot = PlotData()
        self.title("Zanieczyszczenia powietrza")
        self.config(height=500, width=550)

        self.can = Canvas(height=400, width=800)
        self.can.grid(columnspan=3, rowspan=7)
        self.can.rowconfigure(7, weight=1)

        self.info_label = Label(
            text="Wybierz daty początku i końca filtrowania",
            font=(style.font_style(), 13),
            borderwidth=1,
        )

        self.grid_propagate(True)
        self.info_label.grid(column=1, row=0)

        self.sep_line_1 = ttk.Separator(orient="vertical").grid(column=1, row=1, sticky="ns", rowspan=11)

        self.sep_line_2 = ttk.Separator(orient="horizontal").grid(column=2, row=2, sticky="ns", columnspan=3)

        self.start_date_label = Label(text="Poniżej wybierz\ndatę początkową", font="8")
        self.start_date_label.grid(column=0, row=1)

        self.end_date_label = Label(text="Poniżej wybierz\ndatę końcową", font="8")
        self.end_date_label.grid(
            column=2,
            row=1,
        )

        self.start_hour_label = Label(text="Poniżej wprowdź\ngodzinę rozpoczęcia\n w formacie '00:00:00'", font="9")
        self.start_hour_label.grid(
            column=0,
            row=4,
        )
        self.end_hour_label = Label(text="Poniżej wprowadź\ngodzinę zakończenia\n w formacie '00:00:00", font="9")
        self.end_hour_label.grid(
            column=2,
            row=4,
        )
        self.air_poll_label = Label(text="Wybierz zanieczyszczenia, które chcesz wyświetlić")
        self.air_poll_label.grid(column=0, row=7)

        self.air_poll_label = Label(text="Wybierz wartości, które chcesz wyświetlić")
        self.air_poll_label.grid(column=2, row=7)

        self.start_date = Calendar(
            font="Raleway 12",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=2021,
            month=11,
            day=1,
        )
        self.start_date.grid(column=0, row=2)

        self.end_date = Calendar(
            font="Raleway 12",
            selectmode="day",
            locale="en_US",
            cursor="hand1",
            year=2022,
            month=3,
            day=1,
        )
        self.end_date.grid(column=2, row=2)

        self.start_time_input_hour = Entry()
        self.start_time_input_hour.insert("222", dt.datetime.now().strftime("%H:%M:%M"))
        self.start_time_input_hour.grid(column=0, row=5)

        self.end_time_input_hour = Entry()
        self.end_time_input_hour.insert("222", dt.datetime.now().strftime("%H:%M:%M"))
        self.end_time_input_hour.grid(column=2, row=5)

        self.checkboxes = ["PM1", "PM2.5", "PM10", "temp", "pressure", "humidity"]

        check_vars = [tk.IntVar() for i in self.checkboxes]

        self.check_box_PM1 = tk.Checkbutton(
            text="PM1",
            variable=check_vars[0],
            onvalue=1,
            offvalue=0,
        )
        self.check_box_PM2_5 = tk.Checkbutton(
            text="PM2.5",
            variable=check_vars[1],
            onvalue=1,
            offvalue=0,
        )
        self.check_box_PM10 = tk.Checkbutton(
            text="PM10",
            variable=check_vars[2],
            onvalue=1,
            offvalue=0,
        )
        self.check_box_temp = tk.Checkbutton(
            text="Temperatura", variable=check_vars[3], onvalue=1, offvalue=0, anchor="w"
        )
        self.check_box_pressure = tk.Checkbutton(
            text="Ciśnienie", variable=check_vars[4], onvalue=1, offvalue=0, anchor="w"
        )
        self.check_box_humidity = tk.Checkbutton(text="Wilgotność", variable=check_vars[5], onvalue=1, offvalue=0)

        self.check_box_PM1.grid(column=1, row=6, sticky="W")
        self.check_box_PM2_5.grid(column=1, row=7, sticky="W")
        self.check_box_PM10.grid(column=1, row=8, sticky="W")
        self.check_box_temp.grid(column=1, row=6, sticky="E")
        self.check_box_pressure.grid(column=1, row=7, sticky="E")
        self.check_box_humidity.grid(column=1, row=8, sticky="E")

        self.plot_button = tk.Button(
            text="Pokaż wykres",
            font=style.font_style(),
            bg=style.btn_bg_style(),
            fg=style.btn_fg_style(),
            height=3,
            width=13,
            relief=style.btn_rlf_style(),
            command=lambda: [
                plot.plot_chart(
                    self.start_date.get_date(),
                    self.start_time_input_hour.get(),
                    self.end_date.get_date(),
                    self.end_time_input_hour.get(),
                    read_check_vars(check_vars),
                ),
            ],
        )

        self.plot_button.grid(column=1, row=2)

        def read_check_vars(check_vars):
            return [i.get() for i in check_vars]


class SetStyle:
    def __init__(self) -> None:
        pass

    @staticmethod
    def btn_bg_style():
        bg = "#91BE7B"
        return bg

    @staticmethod
    def btn_fg_style():
        fg = "#000000"
        return fg

    @staticmethod
    def btn_rlf_style():
        rlf = RAISED
        return rlf

    @staticmethod
    def full_btn_style(bg, fg, rlf):

        style = [bg, fg, rlf]

        return style

    @staticmethod
    def font_style():
        font = "Raleway"
        return font


if __name__ == "__main__":
    app = Gui()
    app.mainloop()
