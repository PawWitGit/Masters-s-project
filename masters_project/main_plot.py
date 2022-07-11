from datetime import date, datetime
from multiprocessing import get_start_method
from sys import displayhook
from tkinter import messagebox
from tracemalloc import start
from numpy import full
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import os
import glob
import datetime as dt


class PlotData:
    def __init__(self) -> None:
        pass

    def format_date(self, selected_start_date, selected_start_time, selected_end_date, selected_end_time) -> list:

        start_date = "{} {}".format(selected_start_date, selected_start_time)
        end_date = "{} {}".format(selected_end_date, selected_end_time)

        times = [start_date, end_date]
        format_dates = []

        for i, val in enumerate(times):
            try:
                format_dates.append(datetime.strptime(times[i], "%d/%m/%y %H:%M:%S"))

            except ValueError:

                format_dates.append(datetime.strptime(times[i], "%m/%d/%y %H:%M:%S"))

        return format_dates

    def selected_values(self, selected_values):
        return selected_values

    @staticmethod
    def plot_chart(selected_start_date, selected_start_time, selected_end_date, selected_end_time, selected_vars):

        plot = PlotData()

        print(plot.selected_values(selected_vars[1]))

        try:
            full_time = plot.format_date(selected_start_date, selected_start_time, selected_end_date, selected_end_time)
        except ValueError:
            messagebox.showwarning(
                "Błąd formatu godziny",
                "Wprowadź godzinę rozpoczęcia i zakończenia filtrowania w poprawnym formacie",
            )

        air_poll_df = pd.read_csv("/home/pi/air_poll_venv/app/air_pollution_smog_1.csv", sep=",")

        for idx, val in enumerate(full_time):
            pd.to_datetime(full_time[idx])

        start_date = full_time[0]
        end_date = full_time[1]

        print("Formatted dates: ")
        print("Start date: {}, type {}".format(start_date, type(start_date)))
        print("End date: {}, type: {}".format(end_date, type(end_date)))

        air_poll_df["date"] = pd.to_datetime(air_poll_df["date"])
        plot_df = (air_poll_df["date"] >= start_date) & (air_poll_df["date"] <= end_date)
        plot_df_2 = air_poll_df.loc[plot_df]

        plot_df_2.plot(x="date", y=["PM1", "PM2.5", "PM10"])

        plt.suptitle(
            "Wartości mierzone przez miernik w okresie\n{} Do {} ".format(start_date, end_date).upper(),
            fontsize=12,
            color="black",
        )

        plt.xlabel("Date -->", fontsize=14, color="black")
        plt.ylabel("Values -->", fontsize=14, color="black")
        plt.show()
