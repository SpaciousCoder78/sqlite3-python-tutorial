#Connecting a database to python 
import sqlite3
#importing sqlite3 module is the first step

conn=sqlite3.connect('enter database name')
#We are creating an object 'conn' to connect the database to python
#Enter the database name in the format 'database.db'

#if the specified file doesn't exist, SQLite creates a new file
