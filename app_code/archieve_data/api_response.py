from typing import NoReturn
import requests
import json


class Response:
    def __init__(
        self,
        response_data,
        response_temp,
        time,
        pm1,
        pm2_5,
        pm10,
        temperature,
        pressure,
        humidity,
        db_array,
    ):

        self.response_data = response_data
        self.response_temp = response_temp
        self.time = time
        self.pm1 = pm1
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.db_array = db_array

    def get_response_data(self) -> None:

        """In this function get response response from sensor api
        and assign them to programm variables"""

        self.response_data = requests.get(
            "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
        ).json()
        self.response_time = requests.get(
            "http://worldtimeapi.org/api/timezone/Europe/Warsaw"
        ).json()

        self.pm1 = self.response_data["feeds"][0]["field1"]
        self.pm2_5 = self.response_data["feeds"][0]["field2"]
        self.pm10 = self.response_data["feeds"][0]["field3"]
        self.temperature = self.response_data["feeds"][0]["field4"]
        self.pressure = self.response_data["feeds"][0]["field5"]
        self.humidity = self.response_data["feeds"][0]["field6"]
        self.time = self.response_time["datetime"]

    def crate_array_to_database(self):

        self.db_array = [
            self.time,
            self.pm1,
            self.pm2_5,
            self.pm10,
            self.temperature,
            self.pressure,
            self.humidity,
        ]

        return self.db_array
