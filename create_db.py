import sqlite3 as sql

#connect to SQLite
con = sql.connect('DATABASE2.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE "DATABASE2" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"MODEL"	TEXT,
	"QTY"	TEXT,
	"PRICE" TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()