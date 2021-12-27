#adding data to the database
import sqlite3


conn=sqlite3.connect('employee.db')


c = conn.cursor()


#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#           pay integer
#            )""")
#We are hashing out the create table command since we have already created a table

#let us now insert values into the table
c.execute("INSERT INTO  employees VALUES('Hoping','Grasshopper',5000)")
#we are inserting values into the table like employee first name, last name and pay
conn.commit()

conn.close()
#if we execute this code, the data gets written into the specified database file
#if you dont get any error in the first run, then the data is successfully inserted into the table

