from numpy import False_
import psycopg2
import time

# from api_response import Response

# create workspace on RPi 4B


def check_db_connect():

    print(time.localtime())

    try:
        conn = psycopg2.connect(
            dbname="measuring",
            user="postgres",
            host="192.168.55.114",
            password="_dataadmin1",
            port="5432",
        )

        conn.close()
        print("DB connection OK\n")

        return True

    except Exception:
        print("DB connection ERROR\n")

        return False


def test_db_connection_are_ok():

    assert check_db_connect() == False
