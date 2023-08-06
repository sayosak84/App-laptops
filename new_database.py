import sqlite3
from sqlite3 import Error
import os


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = conn.close()

    try:
        database = os.path.realpath('test.db')
        conn = sqlite3.connect(database)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def drop_table():

    conn = sqlite3.connect('test.db')
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM laptops")
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    #drop_table()
    #create_connection()
