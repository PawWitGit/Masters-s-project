import json
from typing import NoReturn
import psycopg2
import requests
import time
from database.response import Response

# create workspace on RPi 4B


class DbConnection:
    def __init__(self):
        # "measuring", "postgres", "192.168.55.114", "_dataadmin1", "5432"
        self.dbname = 'measuring'
        self.user = 'postgres'
        self.host = '192.168.55.114'
        self.password = '_dataadmin1'
        self.db_port = '5432'
        self.response = Response(
            requests.get(
                "https://api.thingspeak.com/channels/1569165/feeds.json?results=2"
            ).json(),
            requests.get(
                "http://api.weatherapi.com/v1/current.json?key=6135b0d4cfec4f9c8eb195114210305&q=Katowice&aqi=no"
            ).json(),
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

    def check_db_connect(self):

        self.response.get_response_data()
        print(self.response.time + ":")

        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
            )

            conn.close()
            print("DB connection OK\n")

            return True

        except Exception:
            print("DB connection ERROR\n")

            return False

    def insert_values_to_db(self):

        """Get values from sensor and insert it`s to DB"""

        self.response.get_response_data()
        print(self.response.time + ":")

        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
            )
            print("DB connection OK")
        except:
            print("DB connection ERROR")

        cursor = conn.cursor()
        psql_insert_query = """ INSERT INTO measuring_data (data, pm1, pm2_5, pm10, temperature, pressure, humidity) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        psql_insert_values = (
            self.response.time,
            self.response.pm1,
            self.response.pm2_5,
            self.response.pm10,
            self.response.temperature,
            self.response.pressure,
            self.response.humidity,
        )

        cursor.execute(psql_insert_query, psql_insert_values)
        conn.commit()
        print("Archive OK\n")
        conn.close()

        return True

    def db_archieve_data(self) -> None:

        while True:
            self.insert_values_to_db()
            time.sleep(5)


