import os
import sqlite3
con =sqlite3.connect("database.db")
cur =con.cursor()
os.chdir("..")
os.system("who am i")
flist= os.listdir()
flist.remove(".git")
flist.remove(".idea")
print(flist)
res =cur.execute("select name from sqlite_master")
dblist =res.fetchall()
dblist = [row[0] for row in dblist]

print(type(dblist),dblist)

for fl in flist:

    if fl not in dblist:
        print(("not in the database "))
        query= f"create table {fl} ( name , size )"
        cur.execute(query)
    else:
        print(f"this Db {fl} is available")d
