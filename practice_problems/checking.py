import sqlite3 

con =sqlite3.connect("new.db")

cur =con.cursor()


cur.execute("create table nikhil ( id int , age int)")

cur.close()