import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect(
            """
            dbname='exampledb' 
            user='pi' 
            host='localhost' 
            password='_admin1' 
            connect_timeout=1 
            
            """
        )

        conn.close()
        print("OK")
        return True

    except:
        print('NOOK')
        return False
        

postgres_test()