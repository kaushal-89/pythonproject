import re
import math

################## ASSIGNMENT 4 -> QUESTION 1 ##################

print(" // QUESTION 1 STARTS // ")

date = "2020-09-27"
valid_date = re.findall("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", date)
print(valid_date)
valid_date = re.search('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date)
print(valid_date)

print(" // QUESTION 1 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 2 ##################

print(" // QUESTION 2 STARTS // ")

SSN = "111-22-3333"
valid_ssn = re.findall("^\d{3}-\d{2}-\d{4}$", SSN)
print(valid_ssn)
valid_ssn = re.search('^\d{3}-\d{2}-\d{4}$', SSN)
print(valid_ssn)

print(" // QUESTION 2 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 3 ##################

print(" // QUESTION 3 STARTS // ")

IP = "10.255.255.255"
valid_ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
if valid_ip.match(IP):
    print("IP is valid")
else:
    print("IP is not valid")

valid_ip = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', IP)
print(valid_ip)

print(" // QUESTION 3 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 4 ##################

print(" // QUESTION 4 STARTS // ")

mail = 'dean@gmail.com'
valid_mail = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',mail)
print(valid_mail)

print(" // QUESTION 4 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 5 ##################

print(" // QUESTION 5 STARTS // ")

class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create an instance of Box.
x = Box(10, 2)

# Print area.
print(x.area())

print(" // QUESTION 5 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 6 ##################

print(" // QUESTION 6 STARTS // ")

class PointNew:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dist = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist

p11 = PointNew(2,3)
p22 = PointNew(4,5)
print(str(p11.distance(p22)))

print(" // QUESTION 6 ENDS // ")

################## ASSIGNMENT 4 -> QUESTION 7 ##################

print(" // QUESTION 7 STARTS // ")

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value: " + str(self.x) + " y-value: " + str(self.y)

    def __add__(self, other):
        p1.x = self.x + other.x
        p1.y = self.y + other.y
        return p1

p1 = Point(3,4)
p2 = Point(2,3)
print (p1+p2)

print(" // QUESTION 7 ENDS // ")














import sqlite3
import os
import sys


con = sqlite3.connect("test.db")
cur = con.cursor()
#cur.execute("CREATE TABLE store (col1, col2, col3, col4);")

with open('493_m5_datasets_v1.0.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['col1'], i['col2'], i['col3'], i['col4']) for i in dr]

cur.executemany("INSERT INTO store (col1, col2, col3, col4) VALUES (?, ?, ?, ?);", to_db)
con.commit()


exit()

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

#conn.close()

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



print(" // QUESTION 11 ENDS // ")