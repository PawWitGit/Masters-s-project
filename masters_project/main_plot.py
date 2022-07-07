from datetime import date, datetime
from multiprocessing import get_start_method
from sys import displayhook
from numpy import full
import pandas as pd
import matplotlib as plt
import os
import glob
import datetime as dt
from tkinter import messagebox


class PlotData:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_date(start_date, end_date, start_time, end_time):

        times = ["{} {}".format(start_date, start_time), "{} {}".format(end_date, end_time)]
        print(times)
        format_times = []

        for index in range(len(times)):
            print("temp: ".format(times[index]))
            try:
                format_times.append(datetime.strptime(times[index], "%d/%m/%y %H:%M:%S"))
                print(format_times[index])
            except ValueError:
                format_times.append(datetime.strptime(times[index], "%m/%d/%y %H:%M:%S"))
                print(format_times[index])

        print("start time: {}\t\nend time: {}".format((format_times[0]), (format_times[1])))
        print("start time: {}\t\nend time: {}".format(type(format_times[0]), type([format_times[1]])))

        # time = datetime.time(time)
        # full_time = datetime.combine(start_date, time)
        # print(full_time)

        return times[0], times[1]

    @staticmethod
    def plot_chart(start_date, end_date):

        air_poll_df = pd.read_csv("/home/pi/air_poll_venv/app/air_pollution_smog.csv", sep=",")
        print(air_poll_df.head())

        # start_date = pd.to_datetime(start_date)
        # end_date = pd.to_datetime(end_date)

        # print(start_date, end_date)
        # air_poll_df["date"] = pd.to_datetime(air_poll_df["date"])
        # new_df = (air_poll_df["date"] >= start_date) & (air_poll_df["date"] <= end_date)
        # df2 = air_poll_df.loc[new_df]
        # plt.figure(figsize=(10, 10))
        # df2.plot(x="date", y=["PM1", "PM2.5"])
        # plt.suptitle("air_poll_read".upper(), fontsize=12, color="black")
        # plt.xlabel("Date -->", fontsize=14, color="green")
        # plt.ylabel("values", fontsize=14, color="red")
        # plt.show()
