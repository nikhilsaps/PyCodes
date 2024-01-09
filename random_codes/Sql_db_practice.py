import sqlite3
#connected the  sqlite to database.db that is  my file ans con is connection tto that file while the  cur is cursor to execute the  query
con=sqlite3.connect("database.db")
cur=con.cursor()

res= cur.execute("SELECT name from sqlite_master where type='table'")

if res.fetchone() is None:
    print("database is empty")
else :
    print("")



