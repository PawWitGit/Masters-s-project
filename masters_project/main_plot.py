from asyncio.log import logger
from datetime import date, datetime
import faulthandler
from multiprocessing import get_start_method
from sys import displayhook
from tkinter import messagebox
from tracemalloc import start
from matplotlib import markers
from numpy import full
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pylab as plt
import os
import glob
import datetime as dt
import logging


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

    def logging_err(self, type_err):

        print("")

        if type_err == "data_plot_err":
            return logger.warn(logging.warning("{} Not selected data to plot".format(datetime.now())))
        elif type_err == "hour_data_err":
            return logger.warn(logging.warning("{} Wrong format".format(datetime.now())))

    def selected_values(self, selected_values):
        return selected_values

    @staticmethod
    def plot_chart(selected_start_date, selected_start_time, selected_end_date, selected_end_time, selected_vars):

        plot = PlotData()

        filter_values = ["PM1", "PM2.5", "PM10", "temp", "pressure", "humidity"]

        bool_values = dict(zip(filter_values, plot.selected_values(selected_vars)))

        filtered_values = []

        for key, val in bool_values.items():
            if val == 1:
                filtered_values.append(key)

        try:
            full_time = plot.format_date(selected_start_date, selected_start_time, selected_end_date, selected_end_time)
        except ValueError:
            messagebox.showwarning(
                "Błąd formatu godziny",
                "Wprowadź godzinę rozpoczęcia i zakończenia filtrowania w poprawnym formacie",
            )
            plot.logging_err("hour_data_err")

        air_poll_df = pd.read_csv("/home/pi/air_poll_venv/app/air_pollution_smog_1.csv", sep=",")

        try:
            for idx, val in enumerate(full_time):
                pd.to_datetime(full_time[idx])

            start_date = full_time[0]
            end_date = full_time[1]

            air_poll_df["date"] = pd.to_datetime(air_poll_df["date"])
            plot_df = (air_poll_df["date"] >= start_date) & (air_poll_df["date"] <= end_date)
            plot_df_2 = air_poll_df.loc[plot_df]

            size_plot_df_2 = plot_df_2.size
            x = np.arange(14)
            y = np.sin(x / 2)

            plt.rcParams["figure.figsize"] = [16.0, 6.0]
            plt.rcParams["figure.autolayout"] = True

            try:

                plot_df_2.plot(x="date", y=filtered_values)
                # plt.step(2200)

                plt.suptitle(
                    "Wartości mierzone przez miernik w okresie\n{} Do {} ".format(start_date, end_date).upper(),
                    fontsize=12,
                    color="black",
                )

                plt.xlabel("Data", fontsize=12, color="black")
                plt.ylabel("Wartości", fontsize=12, color="black")
                plt.show()
            except TypeError:
                messagebox.showinfo("Błąd danych", "Nie zaznaczyłeś żadnych danych do wyświetlenia"),
                plot.logging_err("data_plot_err")

        except UnboundLocalError:
            pass
