from datetime import datetime
from multiprocessing import get_start_method
from sys import displayhook
import pandas as pd
import matplotlib as plt
import os
import glob


class PlotData:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_start_date(start_date):

        try:
            start_date = datetime.strptime(start_date, "%d/%m/%y")
        except ValueError:
            start_date = datetime.strptime(start_date, "%m/%d/%y")

        print("Start date: {}".format(start_date))
        print(type(start_date))

        return start_date

    @staticmethod
    def get_end_date(end_date):

        try:
            end_date = datetime.strptime(end_date, "%d/%m/%y")
        except ValueError:
            end_date = datetime.strptime(end_date, "%m/%d/%y")

        print("End date: {}".format(end_date))
        print(type(end_date))

        return end_date

    @staticmethod
    def plot_chart(start_date, end_date):

        df = pd.read_csv("home/pi/air_poll_venv/app/air_pulltion_smog.csv")
        print(df.head())
        # air_poll_df = open(r"air_pollution_smog.csv")
        # # pd.read_csv("air_pollution_smog.csv")

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
