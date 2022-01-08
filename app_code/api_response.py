import requests
import json


class Response:
    def __init__(
        self, response_data, pm1, pm2_5, pm10, temperature, pressure, humidity, time
    ):

        self.response_data = response_data
        self.pm1 = pm1
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.time = time

    def get_response_data(self):

        self.pm1 = self.response_data["feeds"][0]["field1"]
        self.pm2_5 = self.response_data["feeds"][0]["field2"]
        self.pm10 = self.response_data["feeds"][0]["field3"]
        self.temperature = self.response_data["feeds"][0]["field4"]
        self.pressure = self.response_data["feeds"][0]["field5"]
        self.humidity = self.response_data["feeds"][0]["field6"]
        self.time = self.response_data["feeds"][0]["created_at"]

        print(self.pm1)
        print(self.pm2_5)
        print(self.pm10)
        print(self.temperature)
        print(self.pressure)
        print(self.humidity)
        print(self.time)

"""TEST REPSPONE"""
ob1 = Response(
    requests.get(
        "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
    ).json(),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)
ob1.get_response_data()
#     def __init__(self, data):
#         self.data = data

#     def print_data(self):
#         print(json.dumps(self.data, indent=4, sort_keys=True))
#         print(self.data["feeds"][0]["field1"])


# obj1 = Response(
#     requests.get(
#         "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
#     ).json()
# )

# obj1.print_data()
