import psycopg2

# create workspace on RPi 4B


class DbConnection:
    def __init__(self, dbname, user, host, password, db_port):

        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password
        self.db_port = db_port

    def connection_to_db(self):

        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
            )

            conn.close()
            print("OK")
            return True

        except:
            print("NOOK")

            return False


obj1 = DbConnection("measuring", "postgres", "localhost", "_dataadmin1", "5432")


obj1.connection_to_db()
