#creating a table
import sqlite3


conn=sqlite3.connect('employee.db')
#lets name our db file as employee.db this time

c = conn.cursor()
#cursor lets us execute SQL commands

#lets create an employee table that has some data
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
#we are creating a table and inserting columns
#the multiple inverted commas are called docstrings
conn.commit()
#commits the current transaction
conn.close()
#we are closing the database

#Running this code will create a table in the specified db file
#If you run the file again, you'll get an error(refer to the image in the repo) saying that the table already, which confirms that the code is working
