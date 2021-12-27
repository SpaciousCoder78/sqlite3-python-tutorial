#Placeholder method of adding objects
emp_1 = Employee('John', 'Doe', 80000)
emp_2= Employee('Jane','Doe', 80000)
#we are making 2 instances and give them some attributes

#We are going to do string formatting using 2 different secure methods
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay))
#First one involves the usage of ? as a placeholder for string, arguements wil be passed onto tuples
c.execute("INSERT INTO employees VALUES (:first, :last, :pay) ", {'first':emp_2.first, "last":emp_2.last,"pass":emp_2.pay})
#This second method will involve the use of dictionaries instead of tuples. Keys will act as placeholders here
