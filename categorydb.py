import psycopg2
import os
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
    # execute a statement
        table_name = 'category'
        os.system('cls')
        col_headers = col_headers = ['category_id', 'name', 'last_update']
        print('{:12}   {:15} {}'.format(*col_headers))
        print('-'*50)
        # get query data
        cur.execute('SELECT * FROM "{}"'.format(table_name))
        data = cur.fetchone()
        print('{:6d}         {:15} {}'.format(*data), end='\n\n')
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
    