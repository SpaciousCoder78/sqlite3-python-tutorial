#Adding python objects to database
import sqlite3
from employee import Employee
#we are calling in the Employee class from the program which we made earlier, they must be in the same directory


conn=sqlite3.connect('sql.db')


c = conn.cursor()


#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#           pay integer
#            )""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2= Employee('Jane','Doe', 80000)

c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay))
#here we are inserting the above instances into the database

c.execute("SELECT * FROM employees WHERE last=?", ('Grasshopper',))
#application of ? placeholder method
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
#application of key placeholder method
print(c.fetchall())



conn.commit()

conn.close()

#executing this code will print the data which was inserted into the database
#check the output in the image file in this folder
