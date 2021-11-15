import requests
import json


class Response:
    def __init__(self, data):
        self.data = data

    def print_data(self):
        print(json.dumps(self.data, indent=4, sort_keys=True))
        print(self.data["feeds"][0]["field1"])


obj1 = Response(
    requests.get(
        "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
    ).json()
)


obj1.print_data()
