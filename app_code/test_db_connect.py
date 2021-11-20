import psycopg2


def postgres_test():

    try:
        conn = psycopg2.connect(
            """
            dbname='measuring' 
            user='postgres' 
            host='localhost' 
            password='_dataadmin1' 
            connect_timeout=1 
            
            """
        )

        conn.close()
        print("OK")
        return True

    except:
        print("NOOK")
        return False


postgres_test()
