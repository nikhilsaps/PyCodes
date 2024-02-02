import sqlite3

con= sqlite3.connect("jmd.db")

cur =con.cursor()

try :
    nik="select age from  sura"
    result=cur.execute(nik).fetchall()
    print(result)
except :
    print("error aa agyi ")

cur.close()



