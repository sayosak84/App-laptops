import sqlite3
from sqlite3 import Error
import os


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    try:
        database = os.path.realpath('test.db')
        conn = sqlite3.connect(database)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()