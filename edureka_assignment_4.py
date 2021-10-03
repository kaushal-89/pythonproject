#Q1
import re
import math

date = "2020-09-27"
valid_date = re.findall("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", date)
print(valid_date)
valid_date = re.search('^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date)
print(valid_date)

#Q2

SSN = "332-88-1111"
valid_ssn = re.findall("^\d{3}-\d{2}-\d{4}$", SSN)
print(valid_ssn)
valid_ssn = re.search('^\d{3}-\d{2}-\d{4}$', SSN)
print(valid_ssn)

#Q3

ip = "192.168.43.98"
valid_ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
if valid_ip.match(ip):
    print("IP is valid")
else:
    print("IP is not valid")

valid_ip = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip)
print(valid_ip)

#Q4

email = 'kaushalroy@gmail.com'
valid_mail = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
print(valid_mail)

#Q5

class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

x = Box(10, 2)
print(x.area())

#Q6

class Points:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dist = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return dist

p1 = Points(2,3)
p2 = Points(4,5)
print(str(p1.distance(p2)))

#Q7

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
