import sqlite3
import os
import sys
import csv

################## ASSIGNMENT 5 -> QUESTION 1 ##################

print(" // QUESTION 1 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print("SQLite version: %s" % data)

print(" // QUESTION 1 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 2 ##################

print(" // QUESTION 2 STARTS // ")

con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

    print("The last Id of the inserted row is ", cur.lastrowid)

print(" // QUESTION 2 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 2 ##################

print(" // QUESTION 3 STARTS // ")

db_filename = 'todo.db'
db_is_new = not os.path.isfile (db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print('Need to create schema')
    print('Creating database')
else:
    print('Database exists, assume schema does, too.')

conn.close()

print(" // QUESTION 3 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 4 ##################

print(" // QUESTION 4 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()

    cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Model TEXT);")
    cur.execute("SELECT * FROM Cars")
    for colinfo in cur.description:
        print(colinfo[0])

print(" // QUESTION 4 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 5 ##################

print(" // QUESTION 5 STARTS // ")

cars = (
 (1, 'Audi', 52642),
 (2, 'Mercedes', 57127),
 (3, 'Skoda', 9000),
 (4, 'Volvo', 29000),
 (5, 'Bentley', 350000),
 (6, 'Hummer', 41400),
 (7, 'Volkswagen', 21600)
)
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

print(" // QUESTION 5 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 6 ##################

print(" // QUESTION 6 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print(row)

print(" // QUESTION 6 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 7 ##################

print(" // QUESTION 7 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))

print(" // QUESTION 7 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 8 ##################

print(" // QUESTION 8 STARTS // ")

uId = 1
uPrice = 62300
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    con.commit()

print("Number of rows updated: %d" % cur.rowcount)

print(" // QUESTION 8 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 9 ##################

print(" // QUESTION 9 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('PRAGMA table_info(Cars)')
    data = cur.fetchall()

    for d in data:
        print(d[0], d[1], d[2])

print(" // QUESTION 9 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 10 ##################

print(" // QUESTION 10 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))
    for row in rows:
        print("%2s %-10s %s" % row)

print(" // QUESTION 10 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 11 ##################

print(" // QUESTION 11 STARTS // ")

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("CREATE TABLE store (col1, col2, col3, col4);")

with open('493_m5_datasets_v1.0.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("INSERT INTO store VALUES (?, ?, ?, ?)",row)

con.commit()

print(" // QUESTION 11 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 12 ##################

print(" // QUESTION 12 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    for row in rows:
        print(row)

print(" // QUESTION 12 ENDS // ")

################## ASSIGNMENT 5 -> QUESTION 13 ##################

print(" // QUESTION 13 STARTS // ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    for colinfo in cur.description:
        print(colinfo[0])

print(" // QUESTION 13 ENDS // ")

