from db_connect import DbConnection


class TestDbConnection:
    def test_db_connection(dbname, user, host, password, db_port):

        test_db = DbConnection(
            "measuring", "postgres", "localhost", "-dataadmin1", "5432"
        )
