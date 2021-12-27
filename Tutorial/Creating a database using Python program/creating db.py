#creating a database by connecting sqlite to python
#if a database doesn't exist, this program will create a new database in the specified path
import sqlite3
#we need to import the module sqlite 3 first
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__=='__main__':
    create_connection(r"C:\Users\USERNAME\Desktop\sql.db")
#mention the name of the database file that needs to be created in the form 'filename.db' at the end of the path