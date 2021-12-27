#querying the database for the inserted values
import sqlite3


conn=sqlite3.connect('employee.db')


c = conn.cursor()


#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#           pay integer
#            )""")

#c.execute("INSERT INTO  employees VALUES('Hoping','Grasshopper',5000)")
#hashing since its not required anymore
#lets create a select statement
c.execute("SELECT * FROM employees WHERE last='Grasshopper'")

#for iterating via query, there are different methods
#fetchone() --> returns only one row, returns none if no more rows avaliable
#fetchmany() --> it takes an argument and returns no of rows as a list
#fetchall() --> returns all the remaining rows as a list

print(c.fetchone())
#fetchone is more suitable for our program 
#lets print the result


conn.commit()

conn.close()
#when you execute the code, it prints out the data in the table
#refer the output in the image file
