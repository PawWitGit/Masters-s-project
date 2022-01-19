"""
Create the unittest db_connection

"""

import pytest
from db_connect import DbConnection


class TestDbConnection:


    def test_db_connection_ok(self):

        db_conn = DbConnection(
            "measuring", "measuring", "postgres", "192.168.55.108", "_dataadmin1", "5432"
        )
        conn = db_conn.check_db_connect(self)

        assert conn == True