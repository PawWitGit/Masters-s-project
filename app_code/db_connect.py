import psycopg2
import requests
import time
from api_response import Response

# create workspace on RPi 4B


class DbConnection:
    def __init__(self, dbname, user, host, password, db_port, response):

        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.db_port = db_port
        self.response = Response(
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
            0,
        )

    def check_db_connect(self):

        self.response.get_response_data()

        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
            )

            conn.close()
            print("OK")
            print(self.response.pm1)

            return True

        except:
            print("NOOK")

            return False

    def insert_values_to_db(self):

        self.response.get_response_data()

        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
            )

        except:
            print("ERROR")

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
        print("Archive OK")
        conn.close()


obj1 = DbConnection("measuring", "postgres", "localhost", "_dataadmin1", "5432", "")
obj1.check_db_connect()
while True:

    obj1.insert_values_to_db()
    time.sleep(60.0)
