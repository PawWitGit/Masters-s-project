import fontTools
import pandas as pd
import matplotlib.pyplot as plt
import csv


class DataView:
    def __init__(self, user_choice) -> None:
        self.input_file = "air_data.csv"
        self.user_choice = user_choice

    def plot_data_from_csv(self, var):

        item_list = [
            "None",
            "None",
            "PM1",
            "PM2.5",
            "PM10",
            "Temperatura",
            "Ciśnienie",
            "Wilgotność",
        ]

        var_list = []
        for i in range(0, len(item_list)):
            var_list.append(item_list[i])

        print(var_list)

        x = []
        y = []

        with open("air_data_plot.csv", "r") as csvfile:
            figure = csv.reader(csvfile, delimiter=",")

            for row in figure:
                x.append(row[1])
                y.append(row[var])

        print("setup var: ", var)
        plt.bar(x, y, color="b", width=0.4)
        plt.xlabel("Date")
        plt.ylabel(str(var_list[var]))
        plt.title("air_data")
        plt.legend()
        plt.xticks(
            rotation=90,
            ha="right",
        )
        plt.tight_layout()
        plt.show()
