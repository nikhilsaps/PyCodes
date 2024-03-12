import sqlite3

con= sqlite3.connect('temp.db')

cur=con.cursor()

cur.execute('create table if not exists user  ( name text, age Int, phone varchar(10))')

cur.close()

